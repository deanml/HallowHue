__author__ = 'Marvin'
from beautifulhue.api import Bridge
import winsound, sys, random, time

def thunder():
    #Play random thunder Sounds
    thunderfnames = ["thunder", "thunder_strike_2", "thunder_strike_3"]
    winsound.PlaySound('resources/%s.wav' % random.choice(thunderfnames), winsound.SND_ASYNC)
    print "In Thunder Method"
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})

    for _ in range(4):
        resource = {'which':2,'data':{'state':{'on':True, "ct":153, 'bri':255, 'alert':'select'}}}
        bridge.light.update(resource)
        resource = {'which':3,'data':{'state':{'on':True, "ct":153, 'bri':255, 'alert':'select'}}}
        bridge.light.update(resource)

    resource = {'which':2,'data':{'state':{'on':True, "hue":46920, "sat":255, 'bri':10}}}
    bridge.light.update(resource)
    resource = {'which':3,'data':{'state':{'on':True, "hue":46920, "sat":255, 'bri':10}}}
    bridge.light.update(resource)

