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
Que reste-t-il à faire : Il faut remplacer les tirets par la lettre trouvée par
l'utilisateur, il faut créer une fonction qui affiche les images suivant le 
nombre d'erreurs faites par le joueur, il faut faire une fonction qui récupère 
les lettres déjà utilisées (global ?), il faut faire une fonction affichant un 
message quand le joueur a finit de jouer car il a gagné ou perdu, il faut 
améliorer la fonction rejouer pour pouvoir raffraichir la page.
"""

#Importation des bibliothèques nécessaires
from tkinter import Tk, Label, Button, Canvas, StringVar, Entry, Frame
from ma_lib_tk import proposition, inconnu, mots, rejouer

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

#Création d'un troisième Frame dans la fenêtre principale
Frame3 = Frame(Mafenetre, relief = 'groove')
Frame3.pack(padx = 10, pady = 10)

Label(Frame1, text = 'Mot à deviner : ').pack(side = 'left')
Mots = StringVar()
Mots.set(mots())
Mot_inconnu = StringVar()
Mot_inconnu.set(inconnu(Mots.get(), ''))
Label(Frame1, textvariable = Mot_inconnu).pack(side = 'left')

Largeur = 200
Longueur = 200
Canevas = Canvas(Frame1, width = Largeur, height = Longueur, bg = 'grey')
Canevas.pack(padx = 5, pady = 5)
photo = []


Lettre = StringVar()
Champ = Entry(Frame2, textvariable = Lettre, bg = 'white', fg = 'black')
Champ.focus_set()
Champ.pack(side = 'left', padx = 5, pady = 5)
buttonLettre = Button(Frame2, text = 'Entrez une lettre', 
                      command = lambda:proposition(Lettre, Champ))
buttonLettre.pack(side = 'top', padx = 25, pady = 25)
lettres_utilisees = StringVar()
lettres_utilisees.set('Lettres déjà utilisées : ')
Label(Frame2, textvariable = lettres_utilisees).pack(side = 'left')

buttonRejouer = Button(Frame3, text = 'Rejouer', 
                       command = lambda: rejouer(Mafenetre))
buttonRejouer.pack(side = 'bottom')


Mafenetre.mainloop()