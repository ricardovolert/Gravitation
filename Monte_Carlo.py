from code_efficace import *
from init_parametres import *
import numpy as np
import sys
sys.stdout = open("Masse.txt", "a")


#Prendre les paramètres d'entrées
i = float(sys.argv[1])
j = float(sys.argv[2])

#Impression d'un message permettant d'afficher l'essai en question
print('\n# Essai {0} - {1}'.format(i,j))

##########################################
#     Définition des valeurs désirées    #
##########################################
dist_max = 10**7 #rayon du cercle dans lequel toutes les planètes sont situées
nbr_planetes = 150
masse_moyenne = i * masse_terre
vitesse_moyenne = 25000
moment_ang_moyen = 2e+33

#Définition de la liste de planètes
liste_planetes = initialize_list(dist_max, nbr_planetes, masse_moyenne, vitesse_moyenne, moment_ang_moyen)

#Exécution du programme
main(liste_planetes)
