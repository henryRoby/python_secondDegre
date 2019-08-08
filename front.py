# -*- coding: Latin-1 -*- 
from tkinter import * 
import math
#Fonction calcul 
def calcul (): 
    #Récupération des variables  
    D=float(A.get()) 
    E=float(B.get()) 
    F=float(C.get()) 
 
    if D == 0 : 
        chaine.configure(text = -F/E)
        
    else : 
        delta = E**2 - 4*D*F

    
        if(delta < 0):
        
            chaine.configure(text = "L'équation n'a pas de solution")
        
        else:
        
            if (delta == 0):
                chaine.configure(text =(-E / (2*D)))
        
            else:
            
                x1 = (-E - math.sqrt(delta)) /(2*D)
                x2 = (-E + math.sqrt(delta)) /(2*D)
                chaine.configure(text = x1)
                chaine1.configure(text = x2)

fenetre = Tk() 
fenetre.title("Test de calculs") 

txt1=Label(fenetre, text="A:").grid(row=1, column=1) 
txt2=Label(fenetre, text='B:').grid(row=2, column=1) 
txt3=Label(fenetre, text='C:').grid(row=3, column=1)
Button(fenetre,text='Solution',command=calcul).grid(row=4 , column=1) 
Button(fenetre,text='Quitter',command=fenetre.destroy).grid(row=4, column=2) 

A=Entry(fenetre) 
B=Entry(fenetre) 
C=Entry(fenetre)
chaine = Label(fenetre) 
chaine1 = Label(fenetre) 

A.grid(row=1, column=2) 
B.grid(row=2, column=2) 
C.grid(row=3, column=2)
chaine.grid(row=5, column=1) 
chaine1.grid(row=5, column=2) 

fenetre.mainloop()