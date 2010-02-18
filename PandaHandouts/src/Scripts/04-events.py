from Panda import *
#This is the contents of the script file
"""
time,sound,create
time,Event,Event
0,sorry,panda
2,whip,sonic
4,evil_laugh,panda
"""

script = loadScript("C:\panda\lib\script4.csv")

def snd(m, v):
    s = sound(v+".wav")
    s.play()

def create(m, v):
    if v == "panda":
        panda(position=P3(localTime, localTime, localTime))
    if v == "sonic":
        sonic(position=P3(-localTime, -localTime, -localTime))

react(script['sound'], snd)
react(script['create'], create)
start()