import glob
import mysql.connector
from datetime import datetime


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
mycursor.execute("CREATE TABLE IF NOT EXISTS capteur4 (id INT AUTO_INCREMENT PRIMARY KEY, temperature VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS hygro1 (id INT AUTO_INCREMENT PRIMARY KEY, humidite VARCHAR(255), horodatage VARCHAR(255), date VARCHAR(255))")
routes_capteurs1 = glob.glob("/sys/bus/w1/devices/28-3c01f0957762/w1_slave")
routes_capteurs2 = glob.glob("/sys/bus/w1/devices/28-3c01f0952eb5/w1_slave")
routes_capteurs3 = glob.glob("/sys/bus/w1/devices/28-3c01f095702b/w1_slave")
routes_capteurs4 = glob.glob("/sys/bus/w1/devices/28-3c01f0950ae4/w1_slave")
horodatage = datetime.now()
horodatage_strg = horodatage.strftime("%H:%M")
horodatage_day = horodatage.strftime("%d-%m")

if len(routes_capteurs1) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs1[0])
    temperature = extraire_temperature(contenu_fichier)
    roundtemp = round(temperature, 2)
    print ("Temperature :", roundtemp, "°")
    print ("Heure :", horodatage_strg)
    print ("Date :", horodatage_day ,"\n")
    sql = "INSERT INTO capteur1 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (roundtemp, horodatage_strg, horodatage_day)
    hum = 100-(roundtemp*2)
    mycursor.execute(sql, val)
    sql2 = "INSERT INTO hygro1 (humidite, horodatage, date) VALUES (%s, %s, %s)"
    val2 = (hum, horodatage_strg, horodatage_day)
    mycursor.execute(sql2, val2)
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

if len(routes_capteurs4) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs1[0])
    temperature = extraire_temperature(contenu_fichier)
    roundtemp = round(temperature, 2)
    print ("Temperature :", roundtemp, "°")
    print ("Heure :", horodatage_strg)
    print ("Date :", horodatage_day ,"\n")
    sql = "INSERT INTO capteur4 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (roundtemp, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()