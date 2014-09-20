import time
from beautifulhue.api import Bridge
from thunder import thunder
from chains import chains
from random import randint
from drone import drone
from godzilla import godzilla
from witch import witch
from heartbeat import heart
from demon import demon
from threading import Thread

def setbasecolors():
    huelist = [46920, 50000, 46920]
    bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':'newdeveloper'})
    lights = bridge.light.get({'which':'all'})
    for light in lights['resource']:
        resource = {'which':light['id'],'data':{'state':{'on':True, 'hue':huelist[light['id']-1] ,'sat':255, 'bri':50}}}
        bridge.light.update(resource)

if __name__ == '__main__':
    while True:
              setbasecolors()
              t = Thread(target=heart)
              t.start()
              time.sleep(20)

              setbasecolors()
              for _ in range(4):
                  t = Thread(target=godzilla)
                  t.start()
                  time.sleep(10)

              setbasecolors()
              for _ in range(5):
                  t = Thread(target=witch)
                  t.start()
                  time.sleep(10)
                  setbasecolors()

              name = "spooky_drone"
              drone(name)

              setbasecolors()
              name = "chains"
              for _ in range(2):
                  t = Thread(target=chains, args=(name,))
                  t.start()
                  time.sleep(10)

              setbasecolors()
              name = "thunder"
              for _ in range(5):
                 t = Thread(target=thunder)
                 t.start()
                 time.sleep(12)

              setbasecolors()
              demon()

              setbasecolors()


