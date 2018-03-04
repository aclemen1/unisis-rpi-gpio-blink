#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import atexit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 18
GPIO.setup(LED, GPIO.OUT)

def switch_off():
  GPIO.output(LED,False)

def switch_on():
  GPIO.output(LED,True)

atexit.register(switch_off)

while True:
  switch_on()
  time.sleep(0.25)
  switch_off()
  time.sleep(0.1)
