#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:22:39 2020

@author: alex
"""

from random import randrange
fich = open('mots.txt','r')

def inconnu(fich, propositions):
    x = ""
    for i in fich:
        if i in propositions:
            x = x + i
        else:
            x = x + "_"
    return x

def proposition(propositions):
 
    while True:
        lettre = input("Choisis une lettre : ")

        if lettre in propositions:
            print("Tu as déjà utilisé cette lettre. Choisis-en une autre !")
        elif lettre not in lettres_mots or len(lettre) != 1:
            print("Met une seule lettre et en minuscule.")
        else:
            break;

    propositions.append(lettre)
    return lettre

nberreurs = len(dessins)-1

def points():
    
    erreurs = 0
    mot = fich[randrange(len(fich))]
    propositions = []

    print(dessins[erreurs])

    while True:
        print("Lettres utilisées :", propositions)
        print("Le mot est :", inconnu(mot, propositions))

        lettre = proposition(propositions)

        if lettre in mot:
            if inconnu(mot, propositions) == mot:
                print("Bravo, tu as trouvé le mot :", mot)
                print("Tu t'es trompé(e) ", erreurs," fois")
                return True
        else:
            erreurs = erreurs + 1
            print(dessins[erreurs])
        if erreurs >= nberreurs:
                print("Tu es pendu, le mot à trouver était :", mot)
                return False
            

parties = 0
victoires = 0


while True:
    parties = parties + 1
    if points():
        victoires = victoires + 1
        
    while True:
        continuer = input("1 pour continuer, 0 pour arrêter : ")
        a=1
        if continuer == '1':
            a = a+1
        elif continuer == '0':
            a = a-1
        break;

    if a == 0:
        break;