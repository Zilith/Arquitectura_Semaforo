from machine import Pin, time_pulse_us, PWM
import time

trigger_pin = Pin(5, Pin.OUT)
echo_pin = Pin(18, Pin.IN)
led_pin = Pin(2, Pin.OUT)
tiempo_espera = 5

servo = PWM(Pin(22, mode=Pin.OUT))
servo.freq(50)

def measure_distance():
    # Generar un pulso de trigger
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()

    # Medir la duración del pulso de eco
    pulse_time = time_pulse_us(echo_pin, 1, 30000)

    # Calcular la distancia en centímetros
    distance_cm = pulse_time / 58
    print(distance_cm)
    return distance_cm

# Bucle principal
while True:
    # Medir la distancia
    distance = measure_distance()

    # Verificar si la distancia es menor o igual a 20 cm
    if distance <= 20:
        servo.duty(80)
        led_pin.on()
        time.sleep(2.5)
        led_pin.off()
        time.sleep(0.25)
        led_pin.on()
        time.sleep(0.25)
        led_pin.off()
        time.sleep(0.25)
        led_pin.on()
        time.sleep(0.25)
    else:
        led_pin.off()
        servo.duty(40)  # Posición inicial


    # Esperar un breve período de tiempo antes de la siguiente medición
    time.sleep(0.1)
