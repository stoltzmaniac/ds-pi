import RPi.GPIO as GPIO


ledPin = 11  # define ledPin
buttonPin = 12 # define buttonPin


def setup():
    GPIO.setmode(GPIO.BOARD)  # use Physical GPIO numbering
    GPIO.setup(ledPin, GPIO.OUT)  # set the ledPin to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set buttonPin to PULL UP INPUT mode
    print(f"Using ledPin {ledPin}")
    print(f"Using buttonPin {buttonPin}")
    

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:  # if buttonPin is pressed
            GPIO.output(ledPin, GPIO.HIGH)  # turn on LED
            print("LED turned on")
        else:  # if button is released
            GPIO.output(ledPin, GPIO.LOW)  # turn off LED
            print("LED turned off")
        
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