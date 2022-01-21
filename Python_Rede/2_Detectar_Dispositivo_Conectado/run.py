from ast import While
import RPi.GPIO as GPIO
from time import sleep
import os


def enviar_ping(ip):
    status = os.system(f"ping {ip} -c 1 -q")
    if status == 0:
        return True
    return False


def controlarLed(estado):
    # Codigo para controlar GPIO
    if estado == True:
        GPIO.output(40, GPIO.HIGH)
    else:
        GPIO.output(40, GPIO.LOW)


def main():
    ip = "0.0.0.0"  # Trocar por IP a ser Trocado
    output_device_pin = 0  # Trocar por PIN de OUTPUT

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output_device_pin, GPIO.OUT)

    while True:
        estado = enviar_ping(ip)
        controlarLed(estado)
        os.system("clear")


if __name__ == "__main__":
    main()
