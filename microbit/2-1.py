# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    # display.show(Image("00300:" "03630:" "36963:" "03630:" "00300"))
    pin1.write_digital(1)
    sleep(1000)
    pin1.write_digital(0)
    sleep(1000)
