import sys
import Adafruit_DHT
import glob
import mysql.connector
from datetime import datetime
import pigpio
import DHT22
from time import sleep

conn = mysql.connector.connect(
		host='localhost',
		user='root',
		password = "couchpass31",
		database='couch_DB',
		)

mycursor = conn.cursor()


pi = pigpio.pi()
DHT1 = DHT22.sensor(pi, 6) # use the actual GPIO pin name
DHT1.trigger()
DHT2 = DHT22.sensor(pi, 19) # use the actual GPIO pin name
DHT2.trigger()
humidity1 = DHT1.humidity()
humidity2 = DHT2.humidity()

mycursor.execute("CREATE TABLE IF NOT EXISTS hygro1 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro2 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
horodatage = datetime.now()
horodatage_strg = horodatage.strftime("%H:%M")
horodatage_day = horodatage.strftime("%d-%m")

if humidity1 == None :
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


if humidity2 == None :
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