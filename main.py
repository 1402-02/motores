import serial
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://motores-8f37a-default-rtdb.firebaseio.com/'
})

serialArduino = serial.Serial("COM11", 9600)



while True:
    ref = db.reference('Grados')
    Datos = str(ref.child('GradosMPP').get())
    Datos2 = str(ref.child('GradosSM').get())
    cadena = Datos+", "+Datos2
    print(cadena)
    time.sleep(2)
    serialArduino.write(cadena.encode('ascii'))
 