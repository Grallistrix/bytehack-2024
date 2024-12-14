import RPi.GPIO as GPIO
import time

servo1PIN = 13 # 33
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1PIN, GPIO.OUT)

servo2PIN = 12 # ?
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo2PIN, GPIO.OUT)

p = GPIO.PWM(servo1PIN, 50) # GPIO 12 for PWM with 50Hz
p.start(2.5) # Initialization

p2 = GPIO.PWM(servo2PIN, 50) # GPIO 12 for PWM with 50Hz
p2.start(2.5) # Initialization
try:
  while True:
    degrees = 2+int(input("Degrees: \n"))/18 #returns Duty cycle values equivalent to inputed degrees (0deg = 2; 180deg = 12)
    p2.ChangeDutyCycle( degrees )
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()