from pyfirmata import Arduino,SERVO
import  time
port='/dev/cu.usbmodem14101'
pin=10
board=Arduino(port)

board.digital[pin].mode=SERVO

def RotateServo(pin,angel):
    board.digital[pin].write(angel)

def DoorAutomate(val):
    if val==0:
        # time.sleep(1.5)
        RotateServo(pin,180)
    if val==1:
        # time.sleep(1.5)
        RotateServo(pin,90)


