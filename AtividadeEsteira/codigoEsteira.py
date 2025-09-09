from machine import Pin, time_pulse_us
import time

# --- Configuração ---
PINO_TRIG = 25
PINO_ECHO = 26

trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)


# --- Contagem ---
contador_itens = 0
contador_caixas = 0
distancia_limite = 10  # Distância em centimetros para detecção do objeto
detectar_ativo = False  # Variável para evitar contagem do mesmo item

# --- Medição de Distância ---
def receber_distancia():
    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)
    if duracao < 0:  
        return 1000  
    distancia = (duracao / 2) * 0.0343
    return distancia

# --- Loop Principal ---
while True:
    dist = receber_distancia()
    print("Distância:", dist, "cm")

    if dist <= distancia_limite:


        if not detectar_ativo:
            contador_itens += 1
            detectar_ativo = True
            print("Item detectado! Total de itens:", contador_itens)

            # Verifica se atingiu 10 itens
            if contador_itens >= 10:
                contador_caixas += 1
                contador_itens = 0  # Zera o contador de itens
                print("Caixa completa! Total de caixas:", contador_caixas)

        time.sleep(1)  # Delay para evitar leituras do mesmo item

    else:
        detectar_ativo = False  # Permite detectar o próximo item

    time.sleep(0.5)
