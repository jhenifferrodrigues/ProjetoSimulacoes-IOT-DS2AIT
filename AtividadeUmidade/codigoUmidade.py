
from machine import Pin, ADC
import time

# Definições dos pinos
PINO_SENSOR_UMIDADE = 34   
PINO_LED_SECO = 26        

# Configuração do sensor 
sensor_umidade = ADC(Pin(PINO_SENSOR_UMIDADE))
sensor_umidade.width(ADC.WIDTH_12BIT)   
sensor_umidade.atten(ADC.ATTN_11DB)

# Configuração do LED
led_seco = Pin(PINO_LED_SECO, Pin.OUT)

# Limiar para considerar "solo seco" (ajuste conforme necessário)
LIMIAR_SECO = 2000

while True:
    # Leitura do valor do sensor
    valor_umidade = sensor_umidade.read()
    print("Valor do sensor:", valor_umidade)

    # Verificação da umidade
    if valor_umidade > LIMIAR_SECO:
        print(" ALERTA: Solo seco! É hora de regar.")
        led_seco.value(1)  # Acende o LED
    else:
        print(" Solo úmido. Tudo certo!")
        led_seco.value(0)  # Apaga o LED

    time.sleep(2)  # Aguarda 

