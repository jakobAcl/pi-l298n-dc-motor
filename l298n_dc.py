# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

from getch import getch, pause
import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
in3 = 21
in4 = 20
ena = 25
enb = 16
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
pwma=GPIO.PWM(ena,1000)
pmwb=GPIO.PWM(enb,1000)

pwma.start(25)
pwmb.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    
print("push 'e' to exit")
print("\n")

while(1):

    x=getch()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'

    elif x=='s':
        print("stop")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'
    elif x=='l':
        print("low")
        pwma.ChangeDutyCycle(25)
        pwmb.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        pwma.ChangeDutyCycle(50)
        pwmb.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        pwma.ChangeDutyCycle(75)
        pwmb.ChangeDutyCycle(75)
        x='z'


    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

