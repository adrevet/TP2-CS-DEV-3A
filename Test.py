#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:59:14 2020

@author: alex
"""
from random import choice

def mots():
    fich = open('mots.txt','r')
    m = fich.readlines()
    for i in range(len(m)-1) :
        m[i] = m[i][:-1]
    word = choice(m)
    fich.close()
    return word
print(mots())
