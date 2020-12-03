# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:55:04 2020

@author: emma
"""

from ELISSALT_Emma_librairie_pendu import fCreationListeMots, fChoisirUnMot, fTesterLettre, fRemplirProposition, fTracerPendu

#2.2.1
nbrTentative=8 #on a initialement 8 tentatives pour trouver le mot
mots=fCreationListeMots()
solution=fChoisirUnMot(mots)
lettreTrouve=[solution[0]] #Pour avoir la premiere lettre dedans
proposition=fRemplirProposition(lettreTrouve, solution)

while ('_' in proposition) and (nbrTentative>0) : #le temps que le mot n'est pas trouvé et qu'il reste des tentatives
    print(proposition)
    print("Il vous reste "+ str(nbrTentative) + " tentatives.") #j'indique au joueur le nombre de tentatives qui lui reste
    lettre = input("Veuillez saisir une lettre : ")[0].upper() #je mets la lettre en masjuscule, car le mot a trouvé est en majuscule et on prend en compte que la premiere lettre saisie
    if fTesterLettre(lettre, solution, lettreTrouve):
        proposition=fRemplirProposition(lettreTrouve, solution)
    else :
        nbrTentative -= 1 #on perd une tentative a chaque fois qu'on a rentre une lettre qui n'est pas dans solution
        fTracerPendu(nbrTentative)

if nbrTentative==0 : #si on est sorti du while est qu'on a plus de tentative ça signifie qu'on a perdu
    print("Vous avez perdu, le mot à trouver était " + solution)
else:
    print("Vous avez gagné, le mot était " + solution)