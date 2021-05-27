from functions import *
import time

offWifi() # Выключить wifi

while True:
    for x in range(100):
        if button.value():
            pokazDanih()
            break

        time.sleep(0.1)
    else:
        pokazDanih()
