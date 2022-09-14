
from cProfile import label
import getpass
from UI import *
from tkinter import filedialog
import tkcap
from PIL import ImageTk, Image
import img2pdf
import pydicom as dicom
import cv2
import csv
import inference

#   METHODS


    

def load_img_file(self):
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select image",
            filetypes=(                
                ("JPEG", "*.jpeg"),
                ("jpg files", "*.jpg"),
                ("png files", "*.png"),
                ("DICOM", "*.dcm"),
            ),
        )
        if filepath:
            global img1
            global array
            array, img2show = read_jpg_file(filepath)
            img1 = img2show.resize((250, 250), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img1)
            return img1

def run_model(self):
            global label
            global img2
            global proba
            label, proba, self.heatmap = inference.predict(self.array)
            img2 = Image.fromarray(self.heatmap)
            img2 = self.img2.resize((250, 250), Image.ANTIALIAS)
            img2 = ImageTk.PhotoImage(self.img2)
            print("OK")
            return label,img2,proba

def save_results_csv(self):
            with open("historial.csv", "a") as csvfile:
                w = csv.writer(csvfile, delimiter="-")
                w.writerow(
                    [self.text1.get(), self.label, "{:.2f}".format(self.proba) + "%"]
                )
                showinfo(title="Guardar", message="Los datos se guardaron con éxito.")


def create_pdf(reportID,root):
            cap = tkcap.CAP(root)
            ID = "Reporte" + str(reportID) + ".jpg"
            img = cap.capture(ID)
            img = Image.open(ID)
            img = img.convert("RGB")
            pdf_path = r"Reporte" + str(reportID) + ".pdf"
            img.save(pdf_path)
            reportID += 1
            showinfo(title="PDF", message="El PDF fue generado con éxito.")

def delete():
            answer = askokcancel(
                title="Confirmación", message="Se borrarán todos los datos.", icon=WARNING
            )
            return answer

    

    

    
