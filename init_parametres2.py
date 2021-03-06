import numpy as np
#from code_efficace import *
from Planet import Planet

#Définition d'une fonction pour évaluer la valeur absolue d'une liste
abs_liste = np.vectorize(abs)

def initialize_list(dist_max, nbr_planetes, masse_moyenne, vitesse_moyenne, moment_ang_moyen,  masse_terre = 5.9722*(10)**24 , rayon_terre = 6378.137 *(10)**3):
    densitee_terre = (masse_terre)/((4*np.pi*rayon_terre**3)/3)

    #########################################
    #   Définition de la liste de planètes  #
    #########################################
    # 1) Masse:
    masse = np.array(abs_liste(np.random.normal(masse_moyenne, masse_moyenne/3, nbr_planetes)))
    masse = masse * (masse_moyenne/masse.mean())

    # 2) Rayon:
    rayon = [(((3*m)/(densitee_terre * 4 * np.pi))**(1/3))/150 for m in masse]

    # 3) Position
    dist = np.random.rand(nbr_planetes) * dist_max
    angle = np.random.rand(nbr_planetes) * 2 * np.pi

    x = [ d * np.cos(theta) for d,theta in zip(dist,angle) ]
    y = [ d * np.sin(theta) for d,theta in zip(dist,angle) ]

    # 4) Vitesse
    vitesse = np.random.normal(vitesse_moyenne, vitesse_moyenne/3, nbr_planetes)
    vitesse = vitesse * (vitesse_moyenne/vitesse.mean())
    angle2 = np.random.rand(nbr_planetes) * 2 * np.pi

    #Définir les vitesse associées
    vx = [v*np.cos(theta2) for v,theta2 in zip(vitesse,angle2)]
    vy = [v*np.sin(theta2) for v,theta2 in zip(vitesse,angle2)]


    # 6) Création des planètes
    liste_planetes = [Planet(masse, rayon, x, y, vx, vy, '{}'.format(i)) for masse,rayon,x,y,vx,vy,i in zip(masse,rayon,x,y,vx,vy,range(1,len(masse)+1))]

    return liste_planetes
