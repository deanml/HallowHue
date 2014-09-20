__author__ = 'Marvin'
from beautifulhue.api import Bridge
import winsound, time

def drone(soundfname):
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})
    lights = bridge.light.get({'which':'all'})
    #Play the Sound
    print "In Drone Method"
    winsound.PlaySound('resources/%s.wav' % soundfname, winsound.SND_ASYNC)
    for _ in range(24):
        time.sleep(1)
        for light in lights['resource']:
            resource = {'which':light['id'],'data':{'state':{'on':True, 'hue':25500 ,'sat':255, "alert":"select"}}}
            bridge.light.update(resource)