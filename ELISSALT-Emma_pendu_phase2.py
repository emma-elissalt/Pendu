# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:55:32 2020

@author: emma
"""

from ELISSALT_Emma_librairie_pendu import fJeuDuPendu

#2.2.2
meilleurScore=8 #qui correspond au plus mauvais score possible
while True :
    score=8-fJeuDuPendu() #pour avoir le nombres de tentatives ratées
    if score < meilleurScore:
        meilleurScore=score
    rep=input('Voulez-vous rejouez? (oui/non) : ') #on lui demande s'il veut rejouer
    if rep=='non': #si c'est non, on sort du while
        break 
#on lui affiche son meilleur score uniquement quand il quitte le jeu
if meilleurScore==0:
    print("Merci d'avoir joué au jeu du pendu. Vous avez tous le temps perdu.")    
else:
    print("Merci d'avoir joué au jeu du pendu, votre meilleur score est d'avoir résolu une énigme avec seulement "+ str(meilleurScore)+" mauvaises tentatives.")