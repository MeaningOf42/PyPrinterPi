import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
while True:
  if (GPIO.input(23)):
    print("Button Pressed")
    time.sleep(0.2)
