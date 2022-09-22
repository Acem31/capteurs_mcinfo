import sys
import Adafruit_DHT
import glob
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
		host='localhost',
		user='root',
		password = "couchpass31",
		database='couch_DB',
		)

mycursor = conn.cursor()

humidity1, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 25)

mycursor.execute("CREATE TABLE IF NOT EXISTS hygro1 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro2 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro3 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro4 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
horodatage = datetime.now()
horodatage_strg = horodatage.strftime("%H:%M")
horodatage_day = horodatage.strftime("%d-%m")

if humidity1 is not None:
   roundhum = round(humidity1, 2)
   print("Humidity=", roundhum,"%")
   sql = "INSERT INTO hygro1 (humidite, horodatage, date) VALUES (%s, %s, %s)"
   val = (roundhum, horodatage_strg, horodatage_day)
   mycursor.execute(sql, val)
   conn.commit()

if humidity1 is not None:
   roundhum = round(humidity1, 2)
   print("Humidity=", roundhum,"%")
   sql = "INSERT INTO hygro2 (humidite, horodatage, date) VALUES (%s, %s, %s)"
   val = (roundhum, horodatage_strg, horodatage_day)
   mycursor.execute(sql, val)
   conn.commit()

if humidity1 is not None:
   roundhum = round(humidity1, 2)
   print("Humidity=", roundhum,"%")
   sql = "INSERT INTO hygro3 (humidite, horodatage, date) VALUES (%s, %s, %s)"
   val = (roundhum, horodatage_strg, horodatage_day)
   mycursor.execute(sql, val)
   conn.commit()

if humidity1 is not None:
   roundhum = round(humidity1, 2)
   print("Humidity=", roundhum,"%")
   sql = "INSERT INTO hygro4 (humidite, horodatage, date) VALUES (%s, %s, %s)"
   val = (roundhum, horodatage_strg, horodatage_day)
   mycursor.execute(sql, val)
   conn.commit()