import time

import RPi.GPIO as GPIO


ledPin = 11  # define ledPin

def setup():
    GPIO.setmode(GPIO.BOARD)  # use Physical GPIO numbering
    GPIO.setup(ledPin, GPIO.OUT)  # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level
    print(f"Using pin {ledPin}")

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH) # make ledPin output HIGH level to turn on LED
        print("LED turned on")
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        print("LED turned off")
        time.sleep(1)
        
def destroy():
    GPIO.cleanup() # release all GPIO

if __name__ == '__main__':
    print('Program Started')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    finally:
        destroy()

