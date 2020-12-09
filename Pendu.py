#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:20:51 2020

@author: alex
"""

# Header
"""
Que fait ce programme : Jeu du pendu version console
Qui l'a fait : Alexandre Drevet
Quand a-t-il été réalisé : 03/12/2020
Que reste-t-il à faire : x
"""

#Importation des bibliothèques nécessaires
from ma_lib import partie

#Programme principal
parties = 0
victoires = 0

#Cette boucle permet de comptabiliser les différentes parties que fait 
#le joueur ainsi que son nombre de victoires et lui demande s'il souhaite 
#continuer ou non
while True:
    parties = parties + 1
    if partie():
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

#Affiche le message de fin lorsque l'utilisateur décide d'arrêter
print("Tu as joué", parties, "partie(s)")
print("Tu en as gagné", victoires)