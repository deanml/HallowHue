__author__ = 'Marvin'
from beautifulhue.api import Bridge
import winsound, sys, random, time

def godzilla():
    #Play random thunder Sounds
    zillafnames = ["godzilla", "godzilla_roar", "godzilla_walking"]
    currfname = random.choice(zillafnames)
    winsound.PlaySound('resources/%s.wav' % currfname, winsound.SND_ASYNC)
    print "In Godzilla Method"
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})

    if currfname == "godzilla_roar":
        for _ in range(5):
            resource = {'which':2,'data':{'state':{'on':True, 'hue':65280, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)
        time.sleep(4)
        for _ in range(5):
            resource = {'which':2,'data':{'state':{'on':True, 'hue':65280, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)

    if currfname == "godzilla":
        for _ in range(5):
            resource = {'which':2,'data':{'state':{'on':True, 'hue':65280, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)
        time.sleep(2)
        for _ in range(5):
            resource = {'which':2,'data':{'state':{'on':True, 'hue':65280, 'alert':'select'}}}
            bridge.light.update(resource)
        for _ in range(5):
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)

    if currfname == "godzilla_walking":
        for _ in range(6):
            resource = {'which':2,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)
            time.sleep(2)
            resource = {'which':3,'data':{'state':{'on':True, 'hue':46920, 'alert':'select'}}}
            bridge.light.update(resource)


