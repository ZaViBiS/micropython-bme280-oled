from functions import *
import time

offWifi() # Выключить wifi


while True:
    if button.value():
        print('temperature : ' + str(temp()))
        print('humidity : ' + str(hum()))
        print('pressure : ' + str(pres()))


    time.sleep(0.1)
