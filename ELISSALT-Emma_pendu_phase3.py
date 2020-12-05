# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:55:32 2020

@author: emma
"""

from ELISSALT_Emma_librairie_pendu import fCreationListeMots,fChoisirUnMot,fRemplirProposition,fTesterLettre
from tkinter import END, Button, ALL, Tk, PhotoImage, Canvas, Label, Frame, FLAT, Entry


#3.1
def rejouer(event):
    global solution
    global lettrePropose
    global lettreTrouve
    global proposition
    nbrTentatives=8
    solution=fChoisirUnMot(mots)
    lettrePropose=[solution[0]] #Pour avoir la première lettre dedans 
    lettreTrouve=[solution[0]] #Pour avoir la première lettre dedans
    proposition=fRemplirProposition(lettreTrouve, solution)
    monCanvas.delete(ALL)
    monCanvas.create_image((largeurImage / 2, hauteurImage / 2), image=mesImages[0])
    monBouton.configure(text="Proposer")
    monBouton.bind("<Button-1>", choisirLettre)
    labelProposition["text"] = "".join(proposition)
    labelTentatives["text"] = "".join("Il vous reste %s tentatives" % nbrTentatives)
    

def choisirLettre(event):
    global nbrTentatives
    global lettreTrouve
    global solution
    global lettrePropose
    global meilleurScore
    lettre = maSaisie.get()[0].upper()
    maSaisie.delete(0,END);
    if lettre in lettrePropose :
        return;        
    lettrePropose+=lettre
    if fTesterLettre(lettre, solution, lettreTrouve):
        lProposition=fRemplirProposition(lettreTrouve, solution)
        labelProposition["text"] = "".join(lProposition)
        if not('_' in lProposition):
            nbErreur = 8-nbrTentatives
            if meilleurScore > nbErreur:
                meilleurScore = nbErreur
            labelTentatives["text"] = "".join("Vous avez gagné avec %d erreurs, votre meilleur score est de %d erreur." % (nbErreur,meilleurScore))
            monBouton.configure(text = "Rejouer")
            monBouton.bind("<Button-1>", rejouer)
    else :
        nbrTentatives = nbrTentatives - 1 #on perd une tentative a chaque fois qu'on a rentre une lettre qui n'est pas dans solution
        monCanvas.delete(ALL)
        monCanvas.create_image((largeurImage / 2, hauteurImage / 2), image=mesImages[8-nbrTentatives])
        if nbrTentatives==0 : #si on est sorti du while est qu'on a plus de tentative ça signifie qu'on a perdu            
            labelTentatives["text"] = "".join("Vous avez perdu. Votre meilleur score est de %s erreurs)" % meilleurScore)
            labelProposition["text"] = "".join(solution)                
        else:
            labelTentatives["text"] = "".join("Il vous reste %s tentatives" % nbrTentatives)
            return

#Initialisation
nbrTentatives=8 #on a initialement 8 tentatives pour trouver le mot
mots=fCreationListeMots()
solution=fChoisirUnMot(mots)
lettrePropose=[solution[0]] #Pour avoir la première lettre dedans 
lettreTrouve=[solution[0]] #Pour avoir la première lettre dedans
proposition=fRemplirProposition(lettreTrouve, solution)
meilleurScore=8

# Création de la fenêtre graphique
maFenetre = Tk()
maFenetre.title("Jeu du pendu - Emma ELISSALT")
#maFenetre.geometry('600x400')
maFenetre.configure(bg='#444644')
    
# Les images
mesImages = [PhotoImage(file="ImagesPendu/bonhomme%s.gif" % j) for j in range(0,nbrTentatives+1)]

# Création de la zone pour afficher les images
largeurImage = mesImages[0].width()
hauteurImage = mesImages[0].height()
monCanvas = Canvas(maFenetre, width=largeurImage, height=hauteurImage, highlightthickness=0)
monCanvas.grid(row=0, column=0, padx=20, pady=20)

#Chargement d'une image
monCanvas.delete(ALL)
monCanvas.create_image((largeurImage / 2, hauteurImage / 2), image=mesImages[0])

#Création d'une frame pour pouvoir mettre le label proposition et tentative 
# l'un au-dessous de l'autre
monCadreLabel = Frame(maFenetre, bg='#444644')
monCadreLabel.grid(row=0, column=1)

# Création des zones de textes : Proposition et Nombre de tentatives restantes
labelProposition = Label(monCadreLabel, font=('Deja Vu Sans Mono', 45, 'bold'), width=26, fg="white")
labelProposition.grid(row=0, column=0)
labelProposition.configure(bg='#444644')

labelTentatives = Label(monCadreLabel, font=('Deja Vu Sans Mono', 14, 'bold'), width=60, fg="white")
labelTentatives.grid(row=1, column=0)
labelTentatives.configure(bg='#444644')

#Création d'une frame pour pouvoir mettre la saisie et le bouton sur la même ligne
monCadreSaisie = Frame(maFenetre, bg='#444644')
monCadreSaisie.grid(row=1, column=1)


# Création de la zone de saisie de la lettre
maSaisie = Entry(monCadreSaisie,  font=('Deja Vu Sans Mono', 20, 'bold'), width=5, bg="white")
maSaisie.grid(row=0, column=0)

# Création du bouton
monBouton = Button(monCadreSaisie, text="Proposer", relief=FLAT, font=('Deja Vu Sans Mono', 14, 'bold'))
monBouton.grid(row=0, column=1, padx=20)
monBouton.bind("<Button-1>", choisirLettre)
    
labelProposition["text"] = "".join(proposition)
labelTentatives["text"] = "".join("Il vous reste %s tentatives" % nbrTentatives)

maFenetre.mainloop()
