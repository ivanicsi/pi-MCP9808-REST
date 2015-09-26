# coding: utf-8
import web
import datetime
from threading import Timer
from time import sleep
import sqlite3
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

sensor = MCP9808.MCP9808()
sensor.begin()

urls = (
    #'/(.+)', 'hello',
    '/', 'hello',
    '/time', 'getTime',
    '/fresh/(.+)', 'fr'
)
app = web.application(urls, globals())
class hello:
    def GET(self):
        name = 'World'
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp = str( round(sensor.readTempC(),2))
        s =  '<!DOCTYPE html> <html> <head> <title>málna pc</title><meta charse$
        s = s + '<body>'
        s = s + '<h1>Hőmérséklet</h1>'
        s = s + '<p>idő:' + now + '</p>'
        s = s + '<pstyle="color:green">hőmérséklet: <strong>' + temp + '°C</str$
        s = s + '</body></html>'
        return s
        #return 'Hello, ' + name + '!' + '\nerdekes\n' + now + '\n' + temp

class getTime:
        def GET(self):
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return now

class fr:
        def GET(self, par):
                return par

if __name__ == "__main__":
    app.run()
