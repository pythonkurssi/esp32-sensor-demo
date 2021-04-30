import dht
from machine import Pin

pin13 = Pin(13, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT11(pin13)


def get_temp_and_humidity():
    sensor.measure()

    return (sensor.temperature(), sensor.humidity())
