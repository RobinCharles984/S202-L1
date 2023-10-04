#Código feito por Tales Machado Prudente

import threading
import time
import random
from pymongo import MongoClient

#Função simulando sensor de temperatura
def tempSensor(nome: str, intervalo: float):
    while True:
        result = sensor.find({"nomeSensor": nome}, {"sensorAlarmado": 1})
        if(bool(result[0]["sensorAlarmado"])):
            print("Atenção! Temperatura muito alta! Verificar " + str(nome) + "!")
        else:
            temp = random.randrange(30, 40)
            print("Sensor: " + str(nome))
            print("A temperatura do sensor é: " + str(temp))
            if(temp > 38):
                alarme = True
                print("Atenção! Temperatura muito alta! Verificar " + str(nome) + "!")
            else:
                alarme = False
            #Passando para o banco de dados    
            sensor.update_one(
                {"nomeSensor": nome},
                {"$set": {"valorSensor": temp, "sensorAlarmado": alarme}}
            )
        time.sleep(intervalo)

client = MongoClient('mongodb+srv://root:root@cluster0.ddrq2fn.mongodb.net/')

db = client['bancoiot']
sensor = db.sensores

#Thread para sensor 1
sensor1 = threading.Thread(target=tempSensor, args=("Sensor 1", 5))
sensor1.start()

#Thread para sensor 2
sensor2 = threading.Thread(target=tempSensor, args=("Sensor 2", 5))
sensor2.start()

#Thread para sensor 3
sensor3 = threading.Thread(target=tempSensor, args=("Sensor 3", 5))
sensor3.start()