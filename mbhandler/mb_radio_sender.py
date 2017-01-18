import radio
from microbit import *

DELAY=100
# Choose a unique name per microbit, max 10 characters
NAME="Niphredil"
radio.config(length = 40)
radio.on()

while True:
    sleep(DELAY)
    x,y,z = accelerometer.get_x(),accelerometer.get_y(),accelerometer.get_z()
    a,b = button_a.is_pressed(),button_b.is_pressed()
    msg = NAME + ':' + str(x) + ':' + str(y) + ':' + str(z) + ':' + str(a) + ':' + str(b)
    radio.send(msg)