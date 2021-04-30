from machine import Pin

pir = Pin(34, Pin.IN)

def handle_motion(pin):
    print('Motion!')

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_motion)
