import time
import RPi.GPIO as GPIO
import sensors.Freenove_DHT as DHT

DHTPin = 11
ledPinBlue = 38
ledPinRed = 40

def setup():
    GPIO.setmode(GPIO.BOARD)  # use Physical GPIO numbering
    GPIO.setup(ledPinBlue, GPIO.OUT)  # set the ledPin to OUTPUT mode
    GPIO.setup(ledPinRed, GPIO.OUT)  # set the ledPin to OUTPUT mode
    GPIO.output(ledPinBlue, GPIO.LOW)  # make ledPin output LOW level
    GPIO.output(ledPinRed, GPIO.LOW)  # make ledPin output LOW level
    print(f"Blue LED Pin: {ledPinBlue}")
    print(f"Red LED Pin: {ledPinRed}")

def loop():
    dht = DHT.DHT(DHTPin)
    sumCnt = 0
        
    while True:
        sumCnt += 1
        chk = dht.readDHT11()  # read DHT11, return value, determine if data read is normal according to return value
#         print(f"The sumCnt is: {sumCnt} \n The chk is: {chk}")
#         if chk is dht.DHTLIB_OK:
#             print("DHT11, OK!")
#         elif chk is dht.DHTLIB_ERROR_CHECKSUM:
#             print("DHTLIB_ERROR_CHECKSUM")
#         elif chck is dht.DHTLIB_ERROR_TIMEOUT:
#             print("DHTLIB_ERROR_TIMEOUT")
#         else:
#             print("Other ERRORS")
#
        if chk is dht.DHTLIB_OK:
            humidity = dht.humidity
            temperature = (9*dht.temperature/5) + 32
            if temperature >= 73:
                GPIO.output(ledPinRed, GPIO.LOW)
                GPIO.output(ledPinBlue, GPIO.HIGH)
            elif temperature < 73:
                GPIO.output(ledPinBlue, GPIO.LOW)
                GPIO.output(ledPinRed, GPIO.HIGH)
            else:
                GPIO.output(ledPinBlue, GPIO.LOW)
                GPIO.output(ledPinRed, GPIO.LOW)
                
            print(f"Humidity: {humidity} \nTemperature: {temperature} \n")
        
        
        
        time.sleep(2)

if __name__ == '__main__':
    print("Program is starting")
    setup()
    try:
        loop()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
    finally:
        GPIO.cleanup()
        exit()
# 

# 
# def loop():
#     while True:
        
#         
# def destroy():
#     GPIO.cleanup() # release all GPIO
# 
# if __name__ == '__main__':
#     print('Program Started')
#     setup()
#     try:
#         loop()
#     except KeyboardInterrupt:
#         destroy()
#     finally:
#         destroy()