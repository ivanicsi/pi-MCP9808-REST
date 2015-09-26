#!/usr/bin/python
# coding: utf-8

from threading import Timer
import datetime
from time import sleep
import sqlite3
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()
        
    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def Measure(name):
    conn = sqlite3.connect('test.db')
    #print "Opened database successfully";
    fo = open("foo.txt", "rw+")
    temp = str( round(sensor.readTempC(),2))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    seq = [now, "\t", temp, "\n"]
    print now + "\t" + temp
    fo.seek(0, 2)
    line = fo.writelines( seq )
    fo.close()
    #now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print now
    conn.execute("INSERT INTO measurement (t,TT_A1,flag)  VALUES ( strftime('%s','"$
    conn.commit()
    conn.close()

print "starting..."
interval = 15  #hány percenként nyomtasson

sensor = MCP9808.MCP9808()
sensor.begin()

t0 = datetime.datetime.now()#.strftime("%Y-%m-%d %H:%M:%S")
delay = ( ( interval - (t0.minute%interval) )*60) - t0.second
print t0.minute , t0.second, delay
sleep(delay)
rt = RepeatedTimer(interval*60, Measure, "World")
print "rt started"
Measure("start")
try:
    while True:
        sleep(1.0) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!
