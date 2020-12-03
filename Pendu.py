#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:20:51 2020

@author: alex
"""

# Header
"""
Que fait ce programme : Jeu du pendu
Qui l'a fait : Alexandre Drevet
Quand a-t--il été réalisé : 03/12/2020
Que reste-t-il à faire : x
"""

#Importation des bibliothèques nécessaires
from ma_lib import inconnu, proposition, points

#Programme principal
lettres-mots = "abcdefghijklmnopqrstuvwxyz"


dessins = [
"""








_|____
""",
"""
 |
 |
 |
 |
 |
 |
 |
_|____
""",
"""
_______
 |   |
 |
 |
 |
 |
 |
 |
_|____
""",
"""
_______
 |   |
 |   O
 |
 |
 |
 |
 |
_|____
""",
"""
_______
 |   |
 |   O
 |   |
 |
 |
 |
 |
_|____
""",
"""
_______
 |   |
 |   O
 |  /|\
 |
 |
 |
 |
_|_____
""",
"""'
_______
 |   |
 |   O
 |  /|\
 |
 |
 |
 |
_|_____
""",
"""
_______
 |   |
 |   O
 |  /|\
 |  /
 |
 |
 |
_|_____
""",
"""
_______
 |   |
 |   O
 |  /|\      GAME OVER
 |  / \
 |
 |
 |
_|_____
"""
]




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