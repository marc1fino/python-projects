import customtkinter
from rembg import remove
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog, ttk
import tkinter
import os
import cv2

images = []
image_count = 0
fn_dir = ""

def pop1():
    global fn_dir
    dirname = 'exp'
    final_dir = os.path.join(os.path.dirname(__file__), dirname)
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)
        image_path = os.path.join(final_dir, 'info.png')
        image_path1 = os.path.join(final_dir, 'icon.ico')
        image1 = Image.open(image_path)
        image2 = Image.open(image_path1)
        image1.save(image_path)
        image2.save(image_path1)
    image_path1 = os.path.join(final_dir, 'icon.ico')
    pop = customtkinter.CTkToplevel(app)
    pop.title("Archivo Guardado con Éxito")
    pop.resizable(False, False)
    pop.after(250, lambda: pop.iconbitmap(image_path1))
    def cerrarventana(event=None):
        pop.destroy()
        pop.update()
    def vieworiginal():
        ruta = os.path.normcase(fn_dir)
        os.system(f'explorer {ruta}')
    info = Image.open(f"{final_dir}/info.png")
    finfo = info.resize((100, 100))
    image = ImageTk.PhotoImage(finfo)
    file_name_label = tkinter.Label(pop, image=image, background="#242424")
    file_name_label.image = image
    file_name_label.grid(column=0, row=0, pady=5, padx=10, rowspan=2)
    file_name_entry = customtkinter.CTkLabel(pop, text="¡Archivo guardado éxitosamente!")
    file_name_entry.grid(column=1, row=0, pady=5, padx=10, columnspan=2)
    file_name_entry.focus_set()
    accept_btn = customtkinter.CTkButton(pop, command=cerrarventana, text="Aceptar", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
    accept_btn.grid(column=2, row=1, pady=5, padx=10)
    open_btn = customtkinter.CTkButton(pop, command=vieworiginal, text="Ver imagen original", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
    open_btn.grid(column=1, row=1, pady=5, padx=10)

    pop.wait_visibility()  # Esperamos a que la ventana sea visible
    pop.grab_set()  # Bloqueamos la ventana principal
    pop.focus_set()  # Establecemos el enfoque en la ventana emergente
    pop.wait_window()
def pop():
    dirname = 'exp'
    final_dir = os.path.join(os.path.dirname(__file__), dirname)
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)
        image_path = os.path.join(final_dir, 'info.png')
        image_path1 = os.path.join(final_dir, 'icon.ico')
        image1 = Image.open(image_path)
        image2 = Image.open(image_path1)
        image1.save(image_path)
        image2.save(image_path1)
    image_path1 = os.path.join(final_dir, 'icon.ico')
    global fn_e
    pop = customtkinter.CTkToplevel(app)
    pop.title("Insertar Nombre")
    pop.resizable(False, False)
    pop.after(250, lambda: pop.iconbitmap(image_path1))
    def cerrarventana(event=None):
        global fn_e
        fn_e = file_name_entry.get()
        if fn_e:
            pop.destroy()
            pop.update()
        
    def cancelarventana(event=None):
        global fn_e
        fn_e = ''
        pop.destroy()
        pop.update()
        
    file_name_label = customtkinter.CTkLabel(pop, text="Inserta un nombre para el archivo:")
    customtkinter.CTkInputDialog
    file_name_label.grid(column=0, row=0, columnspan=2, padx=20, pady=20, sticky="ew")
    file_name_entry = customtkinter.CTkEntry(pop)
    file_name_entry.grid(column=0, row=1, columnspan=2, padx=20, pady=(0, 20), sticky="ew")
    file_name_entry.focus_set()
    accept_btn = customtkinter.CTkButton(pop, command=cerrarventana, text="Aceptar", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
    accept_btn.grid(column=0, row=2, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew")
    cancel_btn = customtkinter.CTkButton(pop, command=cancelarventana, text="Cancelar", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
    cancel_btn.grid(column=1, row=2, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew")

    pop.wait_visibility()  # Esperamos a que la ventana sea visible
    pop.grab_set()  # Bloqueamos la ventana principal
    pop.focus_set()  # Establecemos el enfoque en la ventana emergente
    pop.wait_window() 
def openfile():
    filenames = filedialog.askopenfilenames(title='Abrir archivo JPG/PNG/JPEG', filetypes=[('Archivos JPG', '*jpg'), ('Archivos PNG', '*png'), ('Archivos JPEG', '*jpeg')])
    for index, file_path in enumerate(filenames):
        try:
            dirname = 'exp'
            final_dir = os.path.join(os.path.dirname(__file__), dirname)
            if not os.path.exists(final_dir):
                os.makedirs(final_dir)
            global image_count, fn_e
            images.append(file_path)
            fn_e = os.path.basename(images[image_count])
            name = fn_e
            input = Image.open(file_path)
            inputr = input.resize((500, 300))
            output = remove(inputr)
            output_path = f"{final_dir}/{name}.png"
            output.save(output_path)
            foutput = Image.open(output_path)
            image = ImageTk.PhotoImage(foutput)
            os.remove(output_path)
            file_tab.add(name)
            file_tab.set(name)
            image_label = tkinter.Label(file_tab.tab(name), image=image, background='#333333')
            image_label.image = image
            image_label.pack()
            image_count += 1
            print('<--------->' + '\n¡Imagen cargada con éxito!' + ' ----> ' + name + '\nNúmero de imagen' + ' ----> ' + f'{image_count}'+ '\nLista de imágenes' + ' ----> ' + f'{images}')
        except Exception as e:
            messagebox.showerror("Error al abrir archivo", "Inserta un nombre para el archivo, tiene que ser único")
            print(e)


def savefile():
    global fn_dir
    try:
        filedir = filedialog.askdirectory(title='Elegir ubicación donde se guardará el archivo', mustexist=True)
        current_image = file_tab.get()
        current_i_index = file_tab.index(current_image)
        input = images[int(current_i_index)]
        finput = Image.open(input)
        output = remove(finput)
        fname = f'{current_image}.png'
        finaldir = os.path.join(filedir, fname)
        output.save(finaldir)
        fn_dir = finaldir
        pop1()
        print('<--------->' + '\n¡Imagen guardada con éxito!' + ' ----> ' + filedir + '\nNúmero de imágen' + ' ----> ' + f'{image_count}'+ '\nLista de imágenes' + ' ----> ' + f'{images}')
    except:
        messagebox.showerror("Error al guardar archivo", "Error inesperado ocurrió al cerrar el archivo, inténtalo de nuevo")

def saveallfiles():
    global fn_e, fn_dir
    for index, file_path in enumerate(images):
        global fn_e
        filedir = filedialog.askdirectory(title='Elegir ubicación donde se guardará el archivo', mustexist=True)
        fn_e = os.path.basename(images[index])
        input_image = Image.open(file_path)
        output = remove(input_image)
        output_path = os.path.join(filedir, f"{fn_e}.png")
        fn_dir = output_path
        output.save(output_path)
        pop1()
        print('<--------->' + '\n¡Imagen guardada con éxito!' + ' ----> ' + output_path + '\nNúmero de imágen' + ' ----> ' + f'{index}'+ '\nLista de imágenes' + ' ----> ' + f'{images}')

def closeallfiles():
    global image_count, current_tab
    try:
        current_tab = file_tab.get()
        while current_tab:
            index_current = file_tab.index(current_tab)
            del images[int(index_current)]
            file_tab.delete(current_tab)
            current_tab = file_tab.get()
            image_count =- 1
            print('<--------->' + '\n¡Imagen cerrada con éxito!' + ' ----> ' + current_tab + '\nNúmero de imágenes ahora' + ' ----> ' + f'{len(images)}'+ '\nLista de imágenes' + ' ----> ' + f'{images}')
    except:
        messagebox.showerror("Error al cerrar archivo", f"Error inesperado ocurrió al cerrar el archivo, inténtalo de nuevo")
def closefile():
    global image_count
    try:
        current_tab = file_tab.get()
        del images[int(file_tab.index(current_tab))]
        file_tab.delete(current_tab)
        image_count -= 1
        print('<--------->' + '\n¡Imagen cerrada con éxito!' + ' ----> ' + current_tab + '\nNúmero de imágenes ahora' + ' ----> ' + f'{len(images)}'+ '\nLista de imágenes' + ' ----> ' + f'{images}')
    except:
        messagebox.showerror("Error al cerrar archivo", f"Error inesperado ocurrió al cerrar el archivo, inténtalo de nuevo")



    

    
# create root with ctk
dirname = 'exp'
final_dir = os.path.join(os.path.dirname(__file__), dirname)
dirname = 'exp'
final_dir = os.path.join(os.path.dirname(__file__), dirname)
if not os.path.exists(final_dir):
    os.makedirs(final_dir)
    image_path = os.path.join(final_dir, 'info.png')
    image_path1 = os.path.join(final_dir, 'icon.ico')
    image1 = Image.open(image_path)
    image2 = Image.open(image_path1)
    image1.save(image_path)
    image2.save(image_path1)
image_path1 = os.path.join(final_dir, 'icon.ico')
customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Eliminar Fondo Imagénes")
app.resizable(False, False)
app.iconbitmap(image_path1)

#widgets
frame = customtkinter.CTkFrame(app)
frame.pack()
file_tab = customtkinter.CTkTabview(frame, width=600, height=375)
file_tab.grid(column=0, row=2, pady=5, padx=10, columnspan=3)
frame2 = customtkinter.CTkFrame(app)
frame2.pack()
ofile_button = customtkinter.CTkButton(frame2, command=openfile, text="Abrir archivos", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
ofile_button.grid(column=0, row=3, pady=5, padx=10)
sfile_button = customtkinter.CTkButton(frame2, command=savefile, text="Guardar archivo", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
sfile_button.grid(column=1, row=3, pady=5, padx=10)
safile_button = customtkinter.CTkButton(frame2, command=saveallfiles, text="Guardar todos los archivos", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
safile_button.grid(column=2, row=3, pady=5, padx=10)
cfile_button = customtkinter.CTkButton(frame2, command=closefile, text="Cerrar archivo", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
cfile_button.grid(column=0, row=4, pady=5, padx=10, columnspan=2)
cafile_button = customtkinter.CTkButton(frame2, command=closeallfiles, text="Cerrar todos los archivos", fg_color='#6a6b6a', hover_color='#424242', text_color='#ffffff', border_color='#0f0000', border_width=1)
cafile_button.grid(column=1, row=4, pady=5, padx=10, columnspan=2)

app.mainloop()