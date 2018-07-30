
# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22

GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25

# Informacoes iniciais
print ("Lendo os valores de temperatura e umidade");

def sensor_dht_loop():
    while(1):
        # Efetua a leitura do sensor
        print('chamou dht loop')
        umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
        #print(type(umid))
        #print(type(temp))
        # Caso leitura esteja ok, mostra os valores na tela
        if umid is not None and temp is not None:
            #print(umid)
            #print(temp)
            print ("Umidade = %.1f%%" % umid)
            print ("Temperatura = %.1fºC" % temp)
            time.sleep(1)
            
        else:
            # Mensagem de erro de comunicacao com o sensor
            print("Falha ao ler dados do DHT11 !!!")
            
            
def sensor_dht_once():
    # Efetua a leitura do sensor
    print('chamou dht once')
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
    #print(type(umid))
    #print(type(temp))
    # Caso leitura esteja ok, mostra os valores na tela
    if umid is not None and temp is not None:
        #print(umid)
        #print(temp)
        print ("Umidade = %.1f%%" % umid)
        print ("Temperatura = %.1fºC" % temp)
        time.sleep(1)
        
    else:
        # Mensagem de erro de comunicacao com o sensor
        print("Falha ao ler dados do DHT11 !!!")
        
def sensor_dht_umid_once():
    # Efetua a leitura do sensor
    print('chamou umid once')
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
    #print(type(umid))
    #print(type(temp))
    # Caso leitura esteja ok, mostra os valores na tela
    if umid is not None and temp is not None:
        #print(umid)
        #print(temp)
        return (umid)
        time.sleep(1)
        
    else:
        # Mensagem de erro de comunicacao com o sensor
        print("Falha ao ler dados do DHT11 !!!")

def sensor_dht_temp_once():
    # Efetua a leitura do sensor
    print('chamou temp once')
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
    #print(type(umid))
    #print(type(temp))
    # Caso leitura esteja ok, mostra os valores na tela
    if umid is not None and temp is not None:
        #print(umid)
        #print(temp)
        return (temp)
        
        
    else:
        # Mensagem de erro de comunicacao com o sensor
        print("Falha ao ler dados do DHT11 !!!") 

##
##
### Programa : Sensor de temperatura DHT11 com Raspberry Pi B+
### Autor : FILIPEFLOP
##
### Carrega as bibliotecas
##import Adafruit_DHT
##import RPi.GPIO as GPIO
##import time
##
### Define o tipo de sensor
##sensor = Adafruit_DHT.DHT11
###sensor = Adafruit_DHT.DHT22
##
##GPIO.setmode(GPIO.BOARD)
##
### Define a GPIO conectada ao pino de dados do sensor
##pino_sensor = 25
##
### Informacoes iniciais
##print ("*** Lendo os valores de temperatura e umidade");
##
##while(1):
##   # Efetua a leitura do sensor
##   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
##   # Caso leitura esteja ok, mostra os valores na tela
##   if umid is not None and temp is not None:
##     print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}n").format(temp, umid);
##     print ("Aguarda 5 segundos para efetuar nova leitura...n");
##     time.sleep(5)
##   else:
##     # Mensagem de erro de comunicacao com o sensor
##     print("Falha ao ler dados do DHT11 !!!")