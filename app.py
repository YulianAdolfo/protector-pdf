from tkinter import *
from tkinter import filedialog as fileChooserWindow
from pathlib import Path
import tkinter
import PyPDF2
from isort import file

currentWorkDirectory = Path.cwd()

criptyPanel = Tk()
criptyPanel.title("Cripty")
criptyPanel.configure(width=300, height=100)
criptyPanel.eval('tk::PlaceWindow . center')
def openFileChooser():
    filename = fileChooserWindow.askopenfilename(initialdir=currentWorkDirectory)
    return filename
def setPasswordToFile(filename):
    def getPasswordAndProtect():
        passwordInText = textboxPassword.get()
        typeDocument = Path(filename).suffix
        if (typeDocument == ".pdf"):
            pdfFiles(passwordInText)
        elif (typeDocument == ".docx"):
            wordFiles(passwordInText)
        else:
            print("error de archivo, no compatible con las extensiones .pdf y docx")
    def wordFiles(passwordInText):
        pass
    def pdfFiles(passwordInText):
        pdf = open(filename,"rb")
        inputPdf = PyPDF2.PdfFileReader(pdf)
        numberPages = inputPdf.numPages
        output = PyPDF2.PdfFileWriter()

        for i in range(numberPages):
            inputPdf = PyPDF2.PdfFileReader(pdf)
            output.addPage(inputPdf.getPage(i))
            output.encrypt(passwordInText)

            with open("ASD.pdf", "wb") as outputStream:
                output.write(outputStream)
        pdf.close()
        print("end")
    filepath = Path(filename)
    passwordTab = Tk()
    passwordTab.title("Cripty | Asigne una contraseña para el archivo: " + "'" + filepath.stem + "'")
    passwordTab.resizable(False, False)
    passwordTab.geometry("500x200")
    passwordTab.eval('tk::PlaceWindow . center')
    # body screen tab: label text
    text = Label(passwordTab, text="Ingrese una contraseña para su archivo", width=100,  font=(24))
    text.pack(pady=10)
    # textbox
    textboxPassword = Entry(passwordTab, justify=tkinter.CENTER, width=50, font=(30), show="")
    textboxPassword.pack(pady=5)
    # button
    buttonSetPassword = Button(passwordTab, text="Proteger documento", justify=tkinter.CENTER, command=getPasswordAndProtect)
    buttonSetPassword.pack(pady=10)
    # ends body screen tab
    passwordTab.mainloop()
selectedFilename = openFileChooser()
setPasswordToFile(selectedFilename)
criptyPanel.mainloop()
