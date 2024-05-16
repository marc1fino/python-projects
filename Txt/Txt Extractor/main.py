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
    outputfile_text.configure(state="normal")

    outputfile_text.delete("1.0", tkinter.END)
    txt = open(filename)
    outputfile_text.insert(tkinter.END, txt.read())
    outputfile_text.configure(state="disabled")


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Extractor de TXT con Python")

title = customtkinter.CTkLabel(app, text="Selecciona un archivo", text_color='#0f0000')
title.pack(padx=10, pady=10)
outputfile_text = customtkinter.CTkTextbox(app)
outputfile_text.pack(padx=10, ipady=85, fill='both')
openfile_button = customtkinter.CTkButton(app, command=openFile, text="Abrir archivo TXT",fg_color='#fa7725', hover_color='#d1631f', text_color='#0f0000', border_color='#0f0000', border_width=1)
openfile_button.pack(pady=10)

app.mainloop()