import os
from pathlib import Path as getPath
from tkinter import DISABLED, Button, Checkbutton, Entry, Label, Tk
from tkinter import filedialog as filechooser
from tkinter import messagebox as message
import tkinter
import PyPDF2
from docx2pdf import convert


class Cripty:
    def getCurrentWorkDirectory(self):
        return getPath.cwd()
    def panelPassword(self, currentDirectoryFile):
        self.file = getPath(currentDirectoryFile).stem
        self.extension = getPath(currentDirectoryFile).suffix
        self.fullPathFile = currentDirectoryFile
        self.mainColorBackground = "#05b3aa"
        if (self.extension == ".docx"):
            message.showinfo(message="---- El documento se convertirá a pdf ----")
        self.panel = Tk()
        self.panel.configure(bg=self.mainColorBackground)
        self.panel.resizable(False, False)
        self.panel.title("Cripty | Asignación de contraseña")
        # center app
        self.panel.geometry("700x160")
        self.panel.eval('tk::PlaceWindow . center')
        # title application
        self.setTitleApp(self.panel)
        self.setTxtBoxForPassword(self.panel)
        self.setCheckbox(self.panel)
        self.setButtonEncrypt(self.panel)
        self.setAuthor(self.panel)
        self.panel.protocol("WM_DELETE_WINDOW", self.closeBackgroundWin)
        self.panel.mainloop()
    def setTitleApp(self, elementTk):
        elementTk = Label(self.panel, text=self.file, font=("Arial",10, "bold"), bg=self.mainColorBackground, foreground="white")
        elementTk.pack(pady=5)
    def setTxtBoxForPassword(self, elementTk):
        self.box = elementTk
        self.box = Entry(self.panel, width=80, justify=tkinter.CENTER, show="*", font=("Arial",10), bg="white")
        self.box.pack(pady=5)
    def setCheckbox(self, elementTk):
        self.check = elementTk
        self.stateCheck = tkinter.BooleanVar(self.check)
        self.check = Checkbutton(self.panel, text="Mostrar caracteres", 
        variable=self.stateCheck, command=self.showCharacters, 
        bg=self.mainColorBackground, 
        foreground="white",
        selectcolor=self.mainColorBackground, 
        font=("Arial", 8), 
        activebackground=self.mainColorBackground,
        activeforeground="white")
        self.check.pack()
    def setButtonEncrypt(self, elementTk):
        self.button = elementTk
        self.button = Button(self.panel, text="Proteger documento", font=("Arial", 10), width=30, command=self.encryptFile, cursor="hand2")
        self.button.pack(pady=10)
    def encryptFile(self):
        password = self.box.get().strip()
        if len(password) >= 3:
            self.button.configure(state=DISABLED, text="Procesado")
            self.box.configure(state=DISABLED)
            self.check.configure(state=DISABLED)
            self.processingDocumentForProtect(password)
        else:
            message.showinfo(message="Debe asignar una contraseña al menos de 3 caracteres")
    def showCharacters(self):
        if(self.stateCheck.get()):
            self.box.configure(show="")
        else:
            self.box.configure(show="*")
    def processingDocumentForProtect(self, password):
        try:
            # create a new name for the file
            filenameProtected = self.file
            path = self.getCurrentWorkDirectory()
            path = str(path).replace("\\", "/")
            path = path + "/" + filenameProtected
            if(self.extension == ".pdf"):
                path = path + " - protected" + self.extension
                self.documentTypePDF(password, path)
            else:
                pathUncryptedFile = path + ".pdf"
                pathEncryptedFile = path + " -protected.pdf"
                self.convertToPdf(pathUncryptedFile)
                self.fullPathFile = pathUncryptedFile
                self.documentTypePDF(password, pathEncryptedFile)
                self.deleteUncryptedFilePDF(pathUncryptedFile)
            self.askIfWantToContinueProtectingDocuments()
        except:
            message.showerror(title="Cripty | Error documento", message="Lo sentimos, ha ocurrido un error desconocido")
            self.askIfWantToContinueProtectingDocuments()
    def askIfWantToContinueProtectingDocuments(self):
        continuingProtecting = message.askyesno(message="!!! El archivo fue protegido exitosamente ¡¡¡\n¿Desea proteger más archivos?")
        self.panel.destroy()
        if continuingProtecting:
            file = self.initFilechooser()
            self.typeOfDocument(file)
        else:
            criptyInteface.destroy()
    def deleteUncryptedFilePDF(self, pathUncryptedFile):
        if (os.path.exists(pathUncryptedFile)):
            os.remove(pathUncryptedFile)
    def documentTypePDF(self, password, updatedName):
        document = open(self.fullPathFile, 'rb')
        #creating reader and writer
        documentReader = PyPDF2.PdfFileReader(document)
        documentWriter = PyPDF2.PdfFileWriter()
        # add pages to writer
        for numPage in range(documentReader.numPages):
            documentWriter.addPage(documentReader.getPage(numPage))
        # encrypt
        documentWriter.encrypt(password)
        encryptedPDF = open(updatedName, "wb")
        documentWriter.write(encryptedPDF)
        encryptedPDF.close()
        document.close()
    def convertToPdf(self, path):
        convert(self.fullPathFile, path)
    def setAuthor(self, elementTk):
        elementTk = Label(self.panel, text="Powered by: Yulian Adolfo Rojas", bg=self.mainColorBackground, foreground="white", font=("Arial", 7, "bold", "italic"))
        elementTk.pack(anchor="w", pady=1)
    def typeOfDocument(self, path):
        if path != "":
            if getPath(path).suffix != ".pdf" and getPath(path).suffix != ".docx":
                message.showerror(title="Cripty | Error de archivo", message="Lo sentimos, el archivo no es compatible con formatos .pdf o docx")
                criptyInteface.destroy()
            else:
                self.panelPassword(path)
        else:
            criptyInteface.destroy()
    def initFilechooser(self):
        return filechooser.askopenfilename(initialdir=criptyYuls.getCurrentWorkDirectory())
    def closeBackgroundWin(self):
        criptyInteface.destroy()
        self.panel.destroy()
criptyYuls = Cripty()
criptyInteface = Tk()
criptyInteface.withdraw()
criptyInteface.configure(width=100, height=100)
fileChooserCripty = criptyYuls.initFilechooser()
criptyYuls.typeOfDocument(fileChooserCripty)
criptyInteface.mainloop()

