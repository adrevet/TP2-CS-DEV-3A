#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:25:37 2020

@author: alex
"""

from random import choice

lettres_mots = "abcdefghijklmnopqrstuvwxyz"

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
    