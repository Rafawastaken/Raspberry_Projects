import RPi.GPIO as GPIO  # Package responsavel por importar pinos do raspberry
from time import sleep  # Package responsavel por criar delays

GPIO.setwarnings(False)  # Ignorar avisos
GPIO.setmode(GPIO.BOARD)  # Usar a pinagem fisica da placa

ledPin = 40  # Pino do LED

# Declarar o ledPin como sendo um OUTPUT e declara estado inicial como LOW
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)

while True:  # Infinte Loop
    GPIO.output(ledPin, GPIO.HIGH)  # Liga o Led
    sleep(1)  # Delay 1 segundo
    GPIO.output(ledPin, GPIO.LOW)  # Desliga o LED
    sleep(1)  # Delay 1 segundo
