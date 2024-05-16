import tkinter
import customtkinter
from tkinter import filedialog
from sys import argv
script = argv

customtkinter.set_appearance_mode("light")

def openFile():
    filename = filedialog.askopenfilename(title="Abrir archivo TXT",
                                          filetypes=[('Archivos TXT', '*.txt')])
    title.configure(text=f'{filename}')

    outputfile_text.delete("1.0", tkinter.END)
    txt = open(filename)
    outputfile_text.insert(tkinter.END, txt.read())
def saveFile():
    text = outputfile_text.get("1.0", tkinter.END)
    filename = filedialog.askopenfilename(title="Guardar archivo TXT",
                                          filetypes=[('Archivos TXT', '*.txt')])
    target = open(filename, 'w')
    target.truncate()
    target.write(text)
    target.close()
    title.configure(text='¡Archivo guardado!')
    
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Editor de TXT con Python")

title = customtkinter.CTkLabel(app, text="Selecciona un archivo", text_color='#0f0000')
title.pack(padx=10, pady=10)
outputfile_text = customtkinter.CTkTextbox(app)
outputfile_text.pack(padx=10, ipady=75, fill='both')
openfile_button = customtkinter.CTkButton(app, command=openFile, text="Abrir archivo TXT",fg_color='#fcf230', hover_color='#e0d72b', text_color='#0f0000', border_color='#0f0000', border_width=1)
openfile_button.pack(pady=5)
save_button = customtkinter.CTkButton(app, command=saveFile, text="Guardar archivo TXT",fg_color='#fcf230', hover_color='#e0d72b', text_color='#0f0000', border_color='#0f0000', border_width=1)
save_button.pack(pady=5)

app.mainloop()