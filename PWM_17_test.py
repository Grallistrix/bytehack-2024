import RPi.GPIO as GPIO
import time

servo2PIN = 23 # ?
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo2PIN, GPIO.OUT)
p2 = GPIO.PWM(servo2PIN, 50) # GPIO 12 for PWM with 50Hz
p2.start(2.5) # Initialization

try:
  while True:
    degrees = 2+int(input("Degrees: \n"))/18 #returns Duty cycle values equivalent to inputed degrees (0deg = 2; 180deg = 12)
    p2.ChangeDutyCycle( degrees )
except KeyboardInterrupt:
  p2.stop()
  GPIO.cleanup()