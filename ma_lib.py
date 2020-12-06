#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:22:39 2020

@author: alex
"""

from random import choice

lettres_mots = "abcdefghijklmnopqrstuvwxyz"
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

def mots():
    fich = open('mots.txt','r')
    m = fich.readlines()
    for i in range(len(m)-1) :
        m[i] = m[i][:-1]
    word = choice(m)
    fich.close()
    return word
    

def inconnu(mots, propositions):
    x = ""
    for i in mots:
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

def partie():
    
    erreurs = 0
    mot = mots() 
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
    return