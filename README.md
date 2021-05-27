# micropython bme280 oled


### Подключение (NODE MCU ESP8266)
#### BME280
vin - 3.3V
GND - GND
SCL - GPIO 0 (D3)
SDA - GPIO 2 (D4)
#### Button
vin - 3.3V
GND - GND
I/O - GPIO 5 (D1)
#### Oled
VDD(vin) - 3.3V
GND - GND
SCK - GPIO 14 (D5)
SDA - GPIO 12 (D6)

## Загрузка файлов в NODE MCU ESP8266
###### linux 

```console
sudo apt install python3 python3-pip esptool
sudo pip3 install mpfshell esptool```

Скачаваете micropython c офицального [сайта](https://micropython.org/)
Переходи в дерикторию с прошивкой

```console
sudo python -m esptool erase_flash
```
##### Переподключите устройство
```console
sudo python -m esptool --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 [Имя файла прошивки]
```
##### Переподключите устройство


```console
git clone https://github.com/ZaViBiS/micropython-bme280-oled.git
cd micropython-bme280-oled
chmod +x put.sh
./put.sh
```
```console
$ ./put.sh  
Connected to esp8266

** Micropython File Shell v0.9.2, sw@kaltpost.de ** 
-- Running on Python 3.9 using PySerial 3.5 --

mpfs [/]> put main.py
mpfs [/]> put functions.py
mpfs [/]> put bmFunc.py
mpfs [/]> put oledFunc.py
mpfs [/]> put oled.py
mpfs [/]> put bm280.py
```
