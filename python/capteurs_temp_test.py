import glob
import mysql.connector
from datetime import datetime

def mysqlconnect():
	conn = mysql.connector.connect(
		host='localhost',
		user='couch_user',
		password = "couchpass",
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

mycursor.execute("CREATE TABLE capteur1 (temperature VARCHAR(255), horodatage VARCHAR(255))")
routes_capteurs = glob.glob("/sys/bus/w1/devices/28*/w1_slave")
horodatage = datetime.now()
horodatage_strg = horodatage.strftime("%X")

if len(routes_capteurs) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs[0])
    temperature = extraire_temperature(contenu_fichier)
    print ("Temperature :", temperature, "°")
    print ("Heure :", horodatage_strg)

sql = "INSERT INTO capteur1 (temperature, horodatage) VALUES (%s, %s)"
val = (temperature, horodatage_strg)
mycursor.execute(sql, val)

else :
    print("Sonde non détectee. Vérifier le branchement, ou rendez-vous dans la section montrant une solution possible")