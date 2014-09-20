__author__ = 'Marvin'
from beautifulhue.api import Bridge
import winsound, sys, time

def chains(soundfname):
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})
    lights = bridge.light.get({'which':'all'})
    #Play the Sound
    print "In Chains Method"
    winsound.PlaySound('resources/%s.wav' % soundfname, winsound.SND_ASYNC)

    for _ in range(70):
        resource = {'which':2,'data':{'state':{'on':True, 'hue':56100 ,'sat':255, 'alert':'select'}}}
        bridge.light.update(resource)


