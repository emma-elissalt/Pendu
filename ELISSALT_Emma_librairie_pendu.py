# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:55:32 2020

@author: emma
"""

import random

#le fichier mots.txt à été classé par taille puis par ordre alphabétique, les mots sont tous en majuscule pour eviter les erreurs d'accents

#Fonction qui va créér en retour la liste des mots contenus dans le fichier mots.txt
#Entrées: aucune
#Sorties: liste des mots du fichier mots.txt
def fCreationListeMots():
    fich=open('mots.txt','r')
    mots=fich.readlines()
    fich.close()
    return mots


#Fonction qui va retourner de façon aléatoire un mot dans le fichier mots.txt
#Entrées: Liste des mots
#Sorties: mot choisi aléatoirement
def fChoisirUnMot(pMots):
    return random.choice(pMots).strip('\n')

#Fonction qui teste si la lettre rentrée par l'utilisateur est dans le mot à trouver (=solution)
# et qui la stocke dans la liste lettreTrouve si c'est le cas
#Entrées: La Lettre choisie, le mot à trouver et la liste des lettres déjà trouvées
#Sorties: Renvoie VRAI si la lettre est dans le mot à trouver sinon renvoie FAUX
def fTesterLettre(pLettre,pSolution,pLettreTrouve):
    if pLettre in pSolution:
        pLettreTrouve += pLettre
        return True
    return False

#Fonction qui va remplir le mot à afficher en fonction des lettres trouvées
#Pour plus de larté, un espace rest ajouté entre les lettres
#Les lettres non trouvées sont remplacées par '_'. 
#Entrées: la liste des lettres déjà trouvées et le mot à trouver.
#Sorties: le mot à affichr en fonction des lettres déjà trouvées.
def fRemplirProposition(pLettreTrouve,pSolution):
    proposition = ""
    for l in pSolution:
        if l in pLettreTrouve :
            proposition += l + ' '
        else :
            proposition += '_ '
    return proposition

#Fonction qui demande une nouvelle lettre à l'utilisateur.
#Il y a vérification que la lettre n'a pas déjà été saisie. Sinon l'utilisateur est averti.
#La liste des lettres proposées est mise à jour.
#Entrées: la liste des lettres déjà proposée
#Sorties: renvoie la lettre choisie
def fSaisieLettre(pLettrePropose):
    while True:
        lettre = input("Veuillez saisir une lettre : ")[0].upper() #on tient compte uniquement de la premiere lettre saisie et on la passe en majuscule
        if lettre in pLettrePropose :
            print("Vous avez déjà proposé cette lettre.")
            print("Liste des lettres déjà proposé ")
            print(pLettrePropose)
        else:
            break
    pLettrePropose+=lettre
    return lettre

#Fonction qui trace le schéma du pendu en fonction du nombre de tentatives
#Entrées: Nombre de tentatvie
#Sorties: rien
def fTracerPendu(pNbrTentative):
    if pNbrTentative==0:
        print(" ________  ")
    if pNbrTentative<=1: 
        print("  | /   |  ")
    if pNbrTentative<=2:
        print("  |/    0  ")
    if pNbrTentative<=3:
        print("  |    /|\ ")
    if pNbrTentative<=4:
        print("  |    /|\ ")
    if pNbrTentative<=5:
        print("  |     ")
    if pNbrTentative<=6:  
        print(" /|\       ")
    if pNbrTentative<=7:
        print("***********\n")

#Fonction qui exécute un jeu du pendu complet
#Entrées: rien
#Sorties: Nombre de tentatives. 0 si echec.
def fJeuDuPendu():
    nbrTentative=8 #on a initialement 8 tentatives pour trouver le mot
    mots=fCreationListeMots()
    solution=fChoisirUnMot(mots)
    lettrePropose=[solution[0]] #Pour avoir la première lettre dedans 
    lettreTrouve=[solution[0]] #Pour avoir la première lettre dedans
    proposition=fRemplirProposition(lettreTrouve, solution)
    while ('_' in proposition) and (nbrTentative>0) : #le temps que le mot n'est pas trouvé et qu'il reste des tentatives
        print(proposition)
        print("Il vous reste "+ str(nbrTentative) + " tentatives.") #j'indique au joueur le nombre de tentatives qui lui reste
        lettre=fSaisieLettre(lettrePropose)
        if fTesterLettre(lettre, solution, lettreTrouve):
            proposition=fRemplirProposition(lettreTrouve, solution)
        else :
            nbrTentative -= 1 #on perd une tentative a chaque fois qu'on a rentre une lettre qui n'est pas dans solution
            fTracerPendu(nbrTentative)
    if nbrTentative==0 : #si on est sorti du while est qu'on a plus de tentative ça signifie qu'on a perdu
        print("Vous avez perdu, le mot à trouver était " + solution)
    else:
        print("Vous avez gagné, le mot était " + solution)
    return nbrTentative
