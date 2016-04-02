import RPi.GPIO as GPIO
import time

#set's up gpio correctly
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)

while True:
  if (GPIO.input(23)):
    print("Button1 Pressed")
    time.sleep(0.2) #waits 0.2 seconds to avoid button bounce

  if (GPIO.input(24)):
    print("Button2 Pressed")
    time.sleep(0.2) #waits 0.2 seconds to avoid button bounce

  if (GPIO.input(25)):
    print("Button3 Pressed")
    time.sleep(0.2) #waits 0.2 seconds to avoid button bounce
