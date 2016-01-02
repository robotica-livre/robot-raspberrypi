from raspirobotboard import *
import RPi.GPIO as GPIO
import time

robot = RaspiRobot()
GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)