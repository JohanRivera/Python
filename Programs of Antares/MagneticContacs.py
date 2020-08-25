import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def OpenorClose(input_signal, magnetic_contact):
    GPIO.setup(input_signal,GPIO.in,pull_up_down=GPIO.PUD_UP)
    if input_signal == GPIO.HIGH:
        return 'Magnetic contact {} open'.format(magnetic_contact)
