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
 |  /|/
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
 |  /|/
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
 |  /|/    GAME OVER
 |  / /
 |
 |
 |
_|_____
"""
]

#Cette fonction permet d'ouvrir le fichier texte où les mots sont contenus
#et d'en choisir un au hasard parmis tous
def mots():
    fich = open('mots.txt','r')
    m = fich.readlines()
    for i in range(len(m)-1) :
        m[i] = m[i][:-1] #on enlève le \n à tous les mots
    word = choice(m)
    fich.close()
    return word
    
#Cette fonction permet de remplacer les lettres à chercher par des _ et les
#remplacer lorsque le joueur en a trouvé une
def inconnu(mots, propositions):
    x = ""
    for i in mots:
        if i in propositions:
            x = x + i
        else:
            x = x + "_ "
    return x

#Cette fonction permet de demander à l'utilisateur une lettre et elle sert de 
#sécurité lorsque le joueur ne met pas un caractère approprié
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

#On compte le nombre d'erreurs en fonction du nombre de dessins
nberreurs = len(dessins)-1

#Cette fonction permet de comptabiliser les erreurs commises par le joueur
def partie():
    
    erreurs = 0
    mot = mots() 
    propositions = []

    print(dessins[erreurs])
#Cette boucle permet d'afficher les différentes lettres utilisées par le
#joueur, afficher le mot à trouver et de dire au joueur s'il a gagné cette
#partie ou non
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