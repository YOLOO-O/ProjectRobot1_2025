from microbit import *

while True:
    for i in range(10):
        display.clear()  # clear display
        display.show(str(i))  # display number
        sleep(1000)  # wait for 1 second