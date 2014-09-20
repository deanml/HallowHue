__author__ = 'Marvin'
from beautifulhue.api import Bridge
import winsound, sys, random, time

def demon():
    #Play random thunder Sounds
    currfname = "scary_demon_haunting"
    winsound.PlaySound('resources/%s.wav' % currfname, winsound.SND_ASYNC)
    print "In demon Method"
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})

    resource = {'which':1,'data':{'state':{'on':True, 'hue':65280, 'sat':255, 'bri':255, 'transitiontime':300}}}
    bridge.light.update(resource)
    resource = {'which':2,'data':{'state':{'on':True, 'hue':25500, 'sat':255, 'bri':255, 'transitiontime':300}}}
    bridge.light.update(resource)
    resource = {'which':3,'data':{'state':{'on':True, 'hue':65280, 'sat':255, 'bri':255, 'transitiontime':300}}}
    bridge.light.update(resource)

    time.sleep(30)