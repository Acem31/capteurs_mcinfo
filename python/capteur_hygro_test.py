import sys
import adafruit_dht
import glob
import board
import mysql.connector
from datetime import datetime
import time


conn = mysql.connector.connect(
		host='localhost',
		user='root',
		password = "couchpass31",
		database='couch_DB',
		)

mycursor = conn.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS hygro1 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro2 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
horodatage = datetime.now()
horodatage_strg = horodatage.strftime("%H:%M")
horodatage_day = horodatage.strftime("%d-%m")

dht1 = adafruit_dht.DHT22(19)
humidity1 = dht1.humidity

if humidity1 == None :
      print ("Humidité :", 0, "%")
      sql = "INSERT INTO hygro1 (humidite, horodatage, date) VALUES (%s, %s, %s)"
      val = (0, horodatage_strg, horodatage_day)
      mycursor.execute(sql, val)
      conn.commit()
else:
   if humidity1  > 0 :
      roundhum = round(humidity1, 2)
      print("Humidity=", roundhum,"%")
      sql = "INSERT INTO hygro1 (humidite, horodatage, date) VALUES (%s, %s, %s)"
      val = (roundhum, horodatage_strg, horodatage_day)
      mycursor.execute(sql, val)
      conn.commit()
   else :
      sql = "INSERT INTO hygro1 (humidite, horodatage, date) VALUES (%s, %s, %s)"
      val = (0, horodatage_strg, horodatage_day)
      mycursor.execute(sql, val)
      conn.commit()

dht2 = adafruit_dht.DHT22(6)
humidity2 = dht2.humidity

if humidity2 == None :
      print ("Humidité :", 0, "%")
      sql = "INSERT INTO hygro2 (humidite, horodatage, date) VALUES (%s, %s, %s)"
      val = (0, horodatage_strg, horodatage_day)
      mycursor.execute(sql, val)
      conn.commit()
else:
   if humidity2  > 0 :
      roundhum = round(humidity2, 2)
      print("Humidity=", roundhum,"%")
      sql = "INSERT INTO hygro2 (humidite, horodatage, date) VALUES (%s, %s, %s)"
      val = (roundhum, horodatage_strg, horodatage_day)
      mycursor.execute(sql, val)
      conn.commit()
   else :
      sql = "INSERT INTO hygro2 (humidite, horodatage, date) VALUES (%s, %s, %s)"
      val = (0, horodatage_strg, horodatage_day)
      mycursor.execute(sql, val)
      conn.commit()