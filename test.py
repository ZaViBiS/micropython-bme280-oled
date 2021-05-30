import json


file = open('data.json')
data = file.read()
file.close()

def rereData(data):
    t = ''
    l = []
    for x in data:
        t += x
        if t[-1] == ']':
            
            normalData = json.loads(t)
            normalData[0] = normalData[0].replace('C', '')
            normalData[1] = normalData[1].replace('hPa', '')


            l.append(normalData)
            t = ''

    return l

print(rereData(data))