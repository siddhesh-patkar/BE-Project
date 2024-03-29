import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class sensorData():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('dht-83e67-firebase-adminsdk-221ft-85f14ad0ff.json')

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://dht-83e67-default-rtdb.firebaseio.com/'
    })

    # As an admin, the app has access to read and write all data, regradless of Security Rules

    def Temperature():
        TemperatureRef = db.reference('Temperature')
        temperature = TemperatureRef.get()
        return temperature

    def Humidity():
        HumidityRef = db.reference('Humidity')
        humidity = HumidityRef.get()
        return humidity

    def HeartRate():
        HeartRateRef = db.reference('Pulse Rate')
        heartRate = HeartRateRef.get()
        return heartRate