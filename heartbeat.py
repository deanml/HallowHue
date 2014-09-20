__author__ = 'Marvin'
from beautifulhue.api import Bridge
import winsound, sys, random, time

def heart():
    #Play random thunder Sounds
    currfname = "heartbeat"
    winsound.PlaySound('resources/%s.wav' % currfname, winsound.SND_ASYNC)
    print "In heartbeat Method"
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})

    for _ in range(20):
        resource = {'which':2,'data':{'state':{'on':True, 'hue':65280, 'sat':255, 'bri':255}}}
        bridge.light.update(resource)
        resource = {'which':2,'data':{'state':{'on':False}}}
        bridge.light.update(resource)
        time.sleep(1)
