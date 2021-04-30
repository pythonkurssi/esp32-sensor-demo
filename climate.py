import dht
from machine import Pin

pin12 = Pin(12, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT11(pin12)

def get_temp_and_humidity():
    sensor.measure()

    return (sensor.temperature(), sensor.humidity())