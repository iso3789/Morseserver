#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
from signal import pause

STATUS_LED=18
TDOT=0.2

code = {"0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----."}

x = LED(STATUS_LED)

def morse(zeichen, led):
    if zeichen not in code:
        print ("Nicht vorhanden")
        return
    for n in code[z]:
        if n == "-":
            x.blink(3*TDOT,TDOT,1,False)
            print("-",end="")
        else:
            x.blink(TDOT,TDOT,1,False)
            print("·",end="")

while True:
    nachricht = input("\nZahl: ")
    if nachricht == "#":
        print("Bye")
        break
    for z in nachricht:
        print("", end="  ")
        morse(z, x)
        sleep(2*TDOT)