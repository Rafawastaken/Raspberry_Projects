from sqlite3 import adapt
from time import sleep
import board  # Utilizaremos a pinagem GPIO
import adafruit_dht

# Defenimos o sensor como sendo o DHT11 conectado ao GPIO21
sensor = adafruit_dht.DHT11(board.D21)

while True:
    try:
        temp = sensor.temperature
        humidade = sensor.humidity
        print(f"Temperatura: {temp}*C \nHumidade: {humidade}%")
        sleep(2)  # Delay 2 segundos por medição

    except RuntimeError as error:
        print("Não foi possivel ler dados\nTentar novamente 3 segundos")
        sleep(3)
