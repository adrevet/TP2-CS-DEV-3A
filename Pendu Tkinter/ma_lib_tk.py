#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:25:37 2020

@author: alex
"""

from random import choice
from tkinter import messagebox

lettres_mots = "abcdefghijklmnopqrstuvwxyz"
lettres_utilisees = []

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
def inconnu(mots, Lettre):
    x = ""
    for i in mots:
        if i in Lettre:
            x = x + i
        else:
            x = x + "_ "
    return x


#Cette fonction sert de sécurité lorsque pour que le joueur ne mette pas de 
#caractères inappropirés
def proposition(Lettre, Champ):
    Lettres = Lettre.get()
    Champ.delete(0, 'end')
    print(Lettre)
    if Lettres in lettres_mots:
        lettres_utilisees.append(Lettres)
        print(lettres_utilisees)
    else:
        messagebox.showwarning('Jeu du pendu', 
                            "Choisissez une autre lettre, elle n'est pas valide")
        
#def partie():
#    erreurs = 0
#    mot = mots()
#    propositions = []

#Cette fonction affiche les images du pendu en fonction des erreurs faites par 
#l'utilisateur        
#def afficheimg():

#Cette fonction permet au joueur de rejouer 
def rejouer (Mafenetre):
    Mafenetre.destroy()
    rejouer(Mafenetre)
    
    
    
    
    