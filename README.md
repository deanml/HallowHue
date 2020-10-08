![Python application](https://github.com/deanml/HallowHue/workflows/Python%20application/badge.svg)

HallowHue
=========

My rewrite of Hue Halloween using Python

I used the Beautifulhue python module to create a similar experience
that you might get with the Hue Halloween mobile application.  I wrote the scripts
using python 2.7.  The code is simple with the main method and entry point in the application 
in the file hallow.py.  Each sound segment has it's own python file.  This is my first 
attempt at using the Hue rest api so be kind.  I found to get lights and sounds synced properly
I had to use some sleeps in the code as well as call some of my sound methods in seperate threads.
It is an easy implementation, all the wav files used in the app are found in the resource folder.

Have Fun.  Feel free to use.
