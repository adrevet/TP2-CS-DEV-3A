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
Quand a-t-il été réalisé : 10/12/2020
Que reste-t-il à faire : Il faut afficher le mot à trouver sous forme de tiret,
il faut créer une fonction qui affiche les images suivant le nombre d'erreurs
faites par le joueur, il faut faire une fonction affichant un message quand le 
joueur a finit de jouer car il a gagné ou perdu.
"""

#Importation des bibliothèques nécessaires
from tkinter import Tk, Label, Button, Canvas, StringVar, Entry, Frame
from ma_lib_tk import proposition, inconnu, mots

#Programme principal

#Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Jeu du pendu')
labelWelcome = Label(Mafenetre, text = 'Bienvenue sur le jeu du pendu', 
                     fg = 'black')
labelWelcome.pack()
buttonQuitter = Button(Mafenetre, text = 'Quitter le pendu', fg = 'black', 
                       command = Mafenetre.destroy)

buttonQuitter.pack(side = 'bottom')

#Création d'un widget Frame dnas la fenêtre principale
Frame1 = Frame(Mafenetre, relief = 'groove')
Frame1.pack(side = 'top', padx = 10, pady = 10)

#Création d'un deuxième widget Frame dans la fenêtre principale
Frame2 = Frame(Mafenetre, relief = 'groove')
Frame2.pack(side = 'bottom', padx = 10, pady = 10)

Label(Frame1, text = 'Mot à deviner : ').pack(side = 'left')
Mots = StringVar(mots())
Label(Frame1, Mots.set(lambda: inconnu(Mots.get(), Lettre))).pack(side = 'left')

Largeur = 200
Longueur = 200
Canevas = Canvas(Frame1, width = Largeur, height = Longueur, bg = 'grey')
Canevas.pack(padx = 5, pady = 5)
#photo = PhotoImage(file = 'bonhomme8.gif')
#item = Canevas.create_image(80,80, image = photo)
Lettre = StringVar()
Champ = Entry(Frame2, textvariable = Lettre, bg = 'white', fg = 'black')
Champ.focus_set()
Champ.pack(side = 'left', padx = 5, pady = 5)
BoutonLettre = Button(Frame2, text = 'Entrez une lettre', 
                      command = lambda:proposition(Lettre, Champ))
BoutonLettre.pack(side = 'top', padx = 25, pady = 25)
Label(Frame2, text = 'Lettres déjà utilisées : ').pack(side = 'left')



Mafenetre.mainloop()

