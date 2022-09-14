#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
import PIL
import numpy as np
import tensorflow as tf
import pydicom as dicom
import Back
import inference
import tkcap

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Herramienta para la detección rápida de neumonía")

        #   BOLD FONT
        fonti = font.Font(weight="bold")

        self.root.geometry("815x560")
        self.root.resizable(0, 0)

        #   LABELS
        self.lab1 = ttk.Label(self.root, text="Imagen Radiográfica", font=fonti)
        self.lab2 = ttk.Label(self.root, text="Imagen con Heatmap", font=fonti)
        self.lab3 = ttk.Label(self.root, text="Resultado:", font=fonti)
        self.lab4 = ttk.Label(self.root, text="Cédula Paciente:", font=fonti)
        self.lab5 = ttk.Label(
            self.root,
            text="SOFTWARE PARA EL APOYO AL DIAGNÓSTICO MÉDICO DE NEUMONÍA",
            font=fonti,
        )
        self.lab6 = ttk.Label(self.root, text="Probabilidad:", font=fonti)

        #   TWO STRING VARIABLES TO CONTAIN ID AND RESULT
        self.ID = StringVar()
        self.result = StringVar()

        #   TWO INPUT BOXES
        self.text1 = ttk.Entry(self.root, textvariable=self.ID, width=10)

        #   GET ID
        self.ID_content = self.text1.get()

        #   TWO IMAGE INPUT BOXES
        self.text_img1 = Text(self.root, width=31, height=15)
        self.text_img2 = Text(self.root, width=31, height=15)
        self.text2 = Text(self.root)
        self.text3 = Text(self.root)

        #   BUTTONS
        self.button1 = ttk.Button(
            self.root, text="Predecir", state="disabled", command=self.Model
        )
        self.button2 = ttk.Button(
            self.root, text="Cargar Imagen", command=self.img_load_UI
        )
        self.button3 = ttk.Button(self.root, text="Borrar", command=self.Limpiar)
        self.button4 = ttk.Button(self.root, text="PDF", command=Back.create_pdf)
        self.button6 = ttk.Button(
            self.root, text="Guardar", command=Back.save_results_csv
        )

        #   WIDGETS POSITIONS
        self.lab1.place(x=110, y=65)
        self.lab2.place(x=545, y=65)
        self.lab3.place(x=500, y=350)
        self.lab4.place(x=65, y=350)
        self.lab5.place(x=122, y=25)
        self.lab6.place(x=500, y=400)
        self.button1.place(x=220, y=460)
        self.button2.place(x=70, y=460)
        self.button3.place(x=670, y=460)
        self.button4.place(x=520, y=460)
        self.button6.place(x=370, y=460)
        self.text1.place(x=200, y=350)
        self.text2.place(x=610, y=350, width=90, height=30)
        self.text3.place(x=610, y=400, width=90, height=30)
        self.text_img1.place(x=65, y=90)
        self.text_img2.place(x=500, y=90)

        #   FOCUS ON PATIENT ID
        self.text1.focus_set()

        #  se reconoce como un elemento de la clase
        self.array = None

        #   NUMERO DE IDENTIFICACIÓN PARA GENERAR PDF
        self.reportID = 0

        #   RUN LOOP
        self.root.mainloop()


    def Model(self):
        global img2
        
        img2,self.label,self.proba=Back.run_model()
        
        self.text_img2.image_create(END, image=img2)
        self.text2.insert(END, self.label)
        self.text3.insert(END, "{:.2f}".format(self.proba)+"%")

    
    
    def Limpiar(self):
        answer = Back.delete()
        if answer:
         self.text1.delete(0, "end")
         self.text2.delete(1.0, "end")
         self.text3.delete(1.0, "end")
         self.text_img1.delete(img1, "end")
         self.text_img2.delete(img2, "end")
         showinfo(title="Borrar", message="Los datos se borraron con éxito")
    
    def img_load_UI(self): ## ob
        global img1
        img1=Back.load_img_file(self)
        self.text_img1.image_create(END, image=img1)
        self.button1["state"] = "enabled"
        return img1           
            

def main():
    my_app = App()
    return 0


if __name__ == "__main__":
    main()
