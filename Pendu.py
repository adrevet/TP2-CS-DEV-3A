#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:20:51 2020

@author: alex
"""

# Header
"""
Que fait ce programme : 
Qui l'a fait : Alexandre Drevet
Quand a-t--il été réalisé : 03/12/2020
Que reste-t-il à faire : 
"""

#Importation des bibliothèques nécessaires
from ma_lib import inconnu, proposition, points

#Programme principal
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
 |  /|
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
 |  /|/
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
 |  /|/      GAME OVER
 |  / /
 |
 |
 |
_|_____
"""
]