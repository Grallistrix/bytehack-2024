import RPi.GPIO as GPIO
import time
import keyboard

servoPIN = 13 # 33
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 13 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    wartosc = keyboard.press_and_release('space')
    print(wartosc)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()