# -- coding: utf-8 --
# script lecture_gif.py
# import codecs
from tkinter import *
# import tkMessageBox as messagebox
# from tkFileDialog import askopenfilename
from tkinter.filedialog import askopenfilename
# from PyPDF2 import PdfFileReader,PdfFileWriter
# import PyPDF2
# from pdfrw import PdfReader
# from classes import PDF
import webbrowser
def Ouvrir():
    filename = askopenfilename(title="Ouvrir une fichier pdf",filetypes=[('pdf files','.pdf'),('all files','.*')])
    webbrowser.open_new(filename)

# Main window
Mafenetre = Tk()
Mafenetre.title("Ouvrir pdf")

# Création d'un widget Menu
menubar = Menu(Mafenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Ouvrir un pdf",command=Ouvrir)

menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)

menubar.add_cascade(label="Aide", menu=menuaide)

# Affichage du menu
Mafenetre.config(menu=menubar)

# Création d'un widget Canvas
Canevas = Canvas(Mafenetre)
Canevas.pack(padx=5,pady=5)


# Utilisation d'un dictionnaire pour conserver une référence
gifdict={}

Mafenetre.mainloop()
# soloi anito le eu amnio line6 io
# from tkinter.filedialog import askopenfilename