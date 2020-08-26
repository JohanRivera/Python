import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def OpenorClose(input_signal):
    GPIO.setup(input_signal,GPIO.IN,GPIO.PUD_UP)
    if GPIO.input(input_signal) == GPIO.HIGH:
        return True
    else:
        return False
