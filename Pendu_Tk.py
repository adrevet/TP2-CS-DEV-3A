#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:21:05 2020

@author: alex
"""

# Header
"""
Que fait ce programme : Jeu du pendu version graphique
Qui l'a fait : Alexandre Drevet
Quand a-t-il été réalisé : 
Que reste-t-il à faire : 
"""

#Importation des bibliothèques nécessaires
from tkinter import Tk, Label, Button, Canvas
#from ma_lib_tk import proposition

#Programme principal
Mafenetre = Tk()
Mafenetre.title('Jeu du pendu')
labelWelcome = Label(Mafenetre, text = 'Bienvenue sur le jeu du pendu', fg = 'black')
labelWelcome.pack()
Largeur = 300
Longueur = 300
Canevas = Canvas(Mafenetre, width = Largeur, height = Longueur, bg = 'grey')
Canevas.pack(padx = 5, pady = 5)
#photo = PhotoImage(file = 'bonhomme8.gif')
#item = Canevas.create_image(80,80, image = photo)
BoutonLettre = Button(Mafenetre, text = 'Entrez une lettre')
BoutonLettre.pack(side = 'top', padx = 5, pady = 5)
buttonQuitter = Button(Mafenetre, text = 'Quitter le pendu', fg = 'black', command = Mafenetre.destroy)
buttonQuitter.pack()
Mafenetre.mainloop()

