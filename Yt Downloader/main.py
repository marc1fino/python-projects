import tkinter
import customtkinter
from pytube import YouTube
from tkinter import filedialog


def startDownloadVideo():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        name = name_entry.get()
        directory = filedialog.askdirectory(title='Escoge una ubicación para el archivo')
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        if name:
            video.download(filename=f'{name}.mp4', output_path=f'{directory}')
        else: 
            video.download(filename=f'{ytObject.title}.mp4', output_path=f'{directory}')
        finishLabel.configure(text="¡Descarga completada!", text_color="white")
    except:
        finishLabel.configure(text="Inserta un enlace de YouTube válido.", text_color="red")

def startDownloadAudio():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()
        name = name_entry.get()
        directory = filedialog.askdirectory(title='Escoge una ubicación para el archivo')

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        if name:
            audio.download(filename=f'{name}.mp3', output_path=f'{directory}')
        else: 
            audio.download(filename=f'{ytObject.title}.mp3', output_path=f'{directory}')
        finishLabel.configure(text="¡Descarga completada!", text_color="white")
    except:
        finishLabel.configure(text="Inserta un enlace de YouTube válido.", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    progressBar.set(float(0)) 
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentatge_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentatge_of_compeletion))
    pPercentatge.configure(text=f'{per}%')
    pPercentatge.update()

    progressBar.set(float(percentatge_of_compeletion) / 100)



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader con Python")

title = customtkinter.CTkLabel(app, text="Adjunta un enlace de YouTube")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

title_2 = customtkinter.CTkLabel(app, text="Escoge un nombre para el archivo")
title_2.pack(padx=10, pady=10)

name_var = tkinter.StringVar()
name_entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=name_var)
name_entry.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPercentatge = customtkinter.CTkLabel(app, text="0%")
pPercentatge.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

downloadmp4 = customtkinter.CTkButton(app, text="Descargar Mp4", command=startDownloadVideo)
downloadmp4.pack(padx=10, pady=10)

downloadmp3 = customtkinter.CTkButton(app, text="Descargar Mp3", command=startDownloadAudio)
downloadmp3.pack(padx=10, pady=10)

app.mainloop()