from machine import Pin
import hcsr04


hcsr = hcsr04.HCSR04(18, 19)


def get_distance():
    return hcsr.distance_cm()


print(get_distance())
