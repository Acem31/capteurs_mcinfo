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
routes_capteurs = glob.glob("/sys/bus/w1/devices/28*/w1_slave")
horodatage = datetime.now()
horodatage_strg = horodatage.strftime("%X")
horodatage_day = horodatage.strftime("%x")

if len(routes_capteurs) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs[0])
    temperature = extraire_temperature(contenu_fichier)
    roundtemp = round(temperature, 2)
    print ("Temperature :", temperature, "°")
    print ("Heure :", horodatage_strg)
    print ("Date :", horodatage_day)
    sql = "INSERT INTO capteur1 (temperature, horodatage, date) VALUES (%s, %s, %s)"
    val = (roundtemp, horodatage_strg, horodatage_day)
    mycursor.execute(sql, val)
    conn.commit()

else :
    print("Sonde non détectee. Vérifier le branchement, ou rendez-vous dans la section montrant une solution possible")


