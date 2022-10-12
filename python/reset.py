import sys
import adafruit_dht
import glob
import board
import mysql.connector
from datetime import datetime
import time


conn = mysql.connector.connect(
		host='mysql_db',
		user='root',
		password = "couchpass31",
		database='couch_DB',
		)

def lire_fichier (emplacement) :
    fichier = open(emplacement)
    contenu = fichier.read()
    fichier.close()
    return contenu


def extraire_temperature (contenu) :
    seconde_ligne = contenu.split("\n")[1]
    donnees_temperature = seconde_ligne.split(" ")[9]
    return float(donnees_temperature[2:]) / 1000

mycursor = conn.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS capteur1 (id INT AUTO_INCREMENT PRIMARY KEY, temperature VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS capteur2 (id INT AUTO_INCREMENT PRIMARY KEY, temperature VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS capteur3 (id INT AUTO_INCREMENT PRIMARY KEY, temperature VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro1 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro2 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
routes_capteurs1 = glob.glob("/sys/bus/w1/devices/28-3c01f0957762/w1_slave")
routes_capteurs2 = glob.glob("/sys/bus/w1/devices/28-3c01f095043a/w1_slave")
routes_capteurs3 = glob.glob("/sys/bus/w1/devices/28-3c01f095702b/w1_slave")

horodatage = datetime.now()
horodatage_strg = horodatage.strftime("%H:%M")
horodatage_day = horodatage.strftime("%d-%m")

mycursor.execute("TRUNCATE TABLE capteur1")
mycursor.execute("TRUNCATE TABLE capteur2")
mycursor.execute("TRUNCATE TABLE capteur3")
mycursor.execute("TRUNCATE TABLE hygro1")
mycursor.execute("TRUNCATE TABLE hygro2")

if len(routes_capteurs1) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs1[0])
    temperature = extraire_temperature(contenu_fichier)
    roundtemp = round(temperature, 2)
    print ("Temperature :", roundtemp, "°")
    print ("Heure :", horodatage_strg)
    print ("Date :", horodatage_day ,"\n")
    sql = "INSERT INTO capteur1 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (roundtemp, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()
else :
    sql = "INSERT INTO capteur1 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (0, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()

if len(routes_capteurs2) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs1[0])
    temperature = extraire_temperature(contenu_fichier)
    roundtemp = round(temperature, 2)
    print ("Temperature :", roundtemp, "°")
    print ("Heure :", horodatage_strg)
    print ("Date :", horodatage_day ,"\n")
    sql = "INSERT INTO capteur2 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (roundtemp, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()
else :
    sql = "INSERT INTO capteur2 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (0, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()

if len(routes_capteurs3) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs1[0])
    temperature = extraire_temperature(contenu_fichier)
    roundtemp = round(temperature, 2)
    print ("Temperature :", roundtemp, "°")
    print ("Heure :", horodatage_strg)
    print ("Date :", horodatage_day ,"\n")
    sql = "INSERT INTO capteur3 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (roundtemp, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()
else :
    sql = "INSERT INTO capteur3 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (0, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()

dht1 = adafruit_dht.DHT22(board.D19)
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

dht2 = adafruit_dht.DHT22(board.D6)
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
