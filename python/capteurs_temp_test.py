import glob
import pymysql
import datetime



def lire_fichier (emplacement) :
    fichier = open(emplacement)
    contenu = fichier.read()
    fichier.close()
    return contenu


def extraire_temperature (contenu) :
    seconde_ligne = contenu.split("\n")[1]
    donnees_temperature = seconde_ligne.split(" ")[9]
    return float(donnees_temperature[2:]) / 1000


routes_capteurs = glob.glob("/sys/bus/w1/devices/28*/w1_slave")
horodatage = datetime.datetime.now()



if len(routes_capteurs) > 0 :
    contenu_fichier = lire_fichier(routes_capteurs[0])
    temperature = extraire_temperature(contenu_fichier)
    print ("Temperature :", temperature, "°")
    print ("Heure :", horodatage("%X"))

else :
    print("Sonde non détectee. Vérifier le branchement, ou rendez-vous dans la section montrant une solution possible")