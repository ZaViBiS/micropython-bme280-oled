import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import itertools
import json

def jsonReader(): # Чтение файла
    with open('data.json') as file:
        data = json.load(file)
    return data

# uTdt = lambda time : datetime.utcfromtimestamp(time).strftime('%H:%M:%S')

def reData():
    data = jsonReader()
    newData = {'temp' : [], 'pres' : []}

    for x in data['temp']:
        novadata = float(x[0].replace('C', ''))
        newData['temp'].append(novadata)

    for x in data['pres']:
        novadata = float(x[0].replace('hPa', ''))
        newData['pres'].append(novadata)

    data = []
    for x in itertools.zip_longest(newData['temp'], newData['pres']):
        data.append(list(x))

    return data

def main():
    data = reData()
    data = pd.DataFrame(data, columns = ['temp', 'pres'])

    plt.subplot(2, 1, 2)
    plt.plot(data['temp'])
    plt.grid()
    plt.title('temp')

    plt.subplot(2, 1, 1)
    plt.plot(data['pres'])
    plt.grid()
    plt.title('pres')

    plt.show()

main()