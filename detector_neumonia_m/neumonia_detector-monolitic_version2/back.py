
import getpass
import ui
from ui import *

import pyautogui
import tkcap
import img2pdf
import pydicom as dicom

import inference as infe

#   METHODS

def load_img_file():
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select image",
            filetypes=(
                ("DICOM", "*.dcm"),
                ("JPEG", "*.jpeg"),
                ("jpg files", "*.jpg"),
                ("png files", "*.png"),
            ),
        )
        if filepath:
            array, img2show = infe.read_dicom_file(filepath)
            img1 = img2show.resize((250, 250), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img1)
            ui.text_img1.image_create(END, image=img1)
            ui.button1["state"] = "enabled"

def run_model(self):
        self.label, self.proba, self.heatmap = infe.predict(self.array)
        self.img2 = Image.fromarray(self.heatmap)
        self.img2 = self.img2.resize((250, 250), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(self.img2)
        print("OK")
        self.text_img2.image_create(END, image=self.img2)
        self.text2.insert(END, self.label)
        self.text3.insert(END, "{:.2f}".format(self.proba) + "%")

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

def delete(self):
        answer = askokcancel(
            title="Confirmación", message="Se borrarán todos los datos.", icon=WARNING
        )
        if answer:
            self.text1.delete(0, "end")
            self.text2.delete(1.0, "end")
            self.text3.delete(1.0, "end")
            self.text_img1.delete(self.img1, "end")
            self.text_img2.delete(self.img2, "end")
            showinfo(title="Borrar", message="Los datos se borraron con éxito")

    

    

    