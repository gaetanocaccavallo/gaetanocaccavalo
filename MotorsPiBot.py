import curses
import RPi.GPIO as GPIO
import time

screen = curses.initscr()
curses.noecho()
curses.cbreak
screen.keypad(True)

Mot1F = 18
Mot1R = 23
Mot2F = 25
Mot2R = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(Mot1F,GPIO.OUT)
GPIO.setup(Mot1R,GPIO.OUT)
GPIO.setup(Mot2F,GPIO.OUT)
GPIO.setup(Mot2R,GPIO.OUT)

try:
    while True:
     char = screen.getch()
     if char == ord('q'):
        break
     if char == ord('w'):
        GPIO.output(Mot1F,GPIO.HIGH)
        GPIO.output(Mot1R,GPIO.LOW)
        GPIO.output(Mot2F,GPIO.HIGH)
        GPIO.output(Mot2R,GPIO.LOW)
     if char == ord('s'):
        GPIO.output(Mot1F,GPIO.LOW)
        GPIO.output(Mot1R,GPIO.HIGH)
        GPIO.output(Mot2F,GPIO.LOW)
        GPIO.output(Mot2R,GPIO.HIGH)
     if char == ord('d'):
        GPIO.output(Mot1F,GPIO.LOW)
        GPIO.output(Mot1R,GPIO.HIGH)
        GPIO.output(Mot2F,GPIO.HIGH)
        GPIO.output(Mot2R,GPIO.LOW)
     if char == ord('a'):
        GPIO.output(Mot1F,GPIO.HIGH)
        GPIO.output(Mot1R,GPIO.LOW)
        GPIO.output(Mot2F,GPIO.LOW)
        GPIO.output(Mot2R,GPIO.HIGH)
     if char == ord('x'):
        GPIO.output(Mot1F,GPIO.LOW)
        GPIO.output(Mot1R,GPIO.LOW)
        GPIO.output(Mot2F,GPIO.LOW)
        GPIO.output(Mot2R,GPIO.LOW)
        
finally:
    GPIO.output(Mot1F,GPIO.LOW)
    GPIO.output(Mot1R,GPIO.LOW)
    GPIO.output(Mot2F,GPIO.LOW)
    GPIO.output(Mot2R,GPIO.LOW)
    curses.nocbreak
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()