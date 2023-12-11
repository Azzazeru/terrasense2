import serial
import time
import pymongo
from datetime import datetime

from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://Aaron:1234567890@cluster0.fsizvua.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(MONGO_URI)

db = client['TerraSenseDB']
collection = db['TerraSenseApp_registro_humedad']

arduino = serial.Serial('COM6', 9600)
time.sleep(2)

dataInt = 0

while True:
    # Leer los datos enviados por Arduino
    prc_humedad = int(arduino.readline().decode().strip())
    humedad_ambiente = int(arduino.readline().decode().strip())
    temperatura_ambiente = int(arduino.readline().decode().strip())

    # Crear un documento para insertar en la base de datos
    nuevo_registro = {
        'prc_humedad': prc_humedad,
        'humedad_ambiente': humedad_ambiente,
        'temperatura_ambiente': temperatura_ambiente,
        'fecha_obtencion': datetime.now()
    }

    # Insertar el nuevo registro en la colección de MongoDB
    result = collection.insert_one(nuevo_registro)

    # print(prc_humedad)
    # print(humedad_ambiente)
    # print(temperatura_ambiente)

    print(f"Datos insertados con el ID: {result.inserted_id}")

    time.sleep(5)  # Esperar 10 segundos antes de la siguiente inserción

