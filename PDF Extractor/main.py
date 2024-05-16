import tkinter, PyPDF2
import customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("light")

def openFile():
    filename = filedialog.askopenfilename(title="Abrir archivo PDF",
                                          filetypes=[('Archivos PDF', '*.pdf')])
    reader = PyPDF2.PdfReader(filename)
    title.configure(text=f'{filename}')
    outputfile_text.configure(state="normal")

    outputfile_text.delete("1.0", tkinter.END)
    page = reader.pages[0]
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        outputfile_text.insert(tkinter.END, page.extract_text())
    outputfile_text.configure(state="disabled")


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Extractor de PDF con Python")

title = customtkinter.CTkLabel(app, text="Selecciona un archivo", text_color='#0f0000')
title.pack(padx=10, pady=10)
outputfile_text = customtkinter.CTkTextbox(app)
outputfile_text.pack(padx=10, ipady=85, fill='both')
openfile_button = customtkinter.CTkButton(app, command=openFile, text="Abrir archivo PDF",fg_color='#FF0000', hover_color='#ba0404', text_color='#0f0000', border_color='#0f0000', border_width=1)
openfile_button.pack(pady=10)

app.mainloop()