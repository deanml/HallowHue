__author__ = 'Marvin'
from beautifulhue.api import Bridge
import winsound, sys, random, time

def witch():
    #Play random thunder Sounds
    witchfnames = ["witch", "cat"]
    currfname = random.choice(witchfnames)
    winsound.PlaySound('resources/%s.wav' % currfname, winsound.SND_ASYNC)
    print "In witch Method"
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})

    if currfname == "witch":
        for _ in range(5):
            resource = {'which':1,'data':{'state':{'on':True, 'hue':36210, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':1,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)

    if currfname == "cat":
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':36210, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)
        time.sleep(4)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':65280, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)
        time.sleep(1)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':65280, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)
        time.sleep(1)
        for _ in range(15):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)