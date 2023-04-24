try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

# set LED with pin for confirming there is a connection active
LED = Pin(16, Pin.OUT)
LED.value(0)
ssid = '**************'
password = '**************'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

LED.value(1)

print(station.ifconfig())
