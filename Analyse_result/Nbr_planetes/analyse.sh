#!/bin/bash

#Trouver tous les essais et ne garder que les infos pertinentes

File_name='Nbr_planete.txt'

for line_number in ` grep -n Essai $File_name | cut -d : -f 1`
do
    #1) Trouver le numéro de l'essai correspondant
    nbr_try=`head -n $line_number $File_name | tail -n 1 | cut -d " " -f 3`

    # Écriture dans le fichier analysé
    echo "$nbr_try planetes" >> analyse_nbr2.txt


    #1) Trouver les infos désirées
    #Numéro des lignes
    let "ligne_interet=$line_number+11"

    #touver les lignes
    head -n $ligne_interet $File_name | tail -n 4 >> analyse_nbr2.txt

    echo " " >> analyse_nbr2.txt

done
