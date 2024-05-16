import tkinter
import customtkinter
from tkinter import ttk
import random
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox


def desc_random():
    desc_random_names = "Destornillador Verde", "Archivador Escolar", "Huevo de Pascua", "Grapadora Roja", "Bolígrafo Negro", "Subrayador Fosforito", "Libro Educativo", "Cojín Suave", "Cuchillo de Cocina", "Taza XXL", "Mapa del Mundo", "Guitarra Eléctrica", "Pack 10 Pósters", "Figura de Acción", "Teclado 60%"
    desc_random = random.choice(desc_random_names)
    return desc_random

def name_random():
    name_random_names = "Marc", "Sergio", "Samuel", "Sandra", "Antonio", "Mohammed", "Pedro", "Santiago", "Lucía", "Juan", "Mike", "Jose", "Paula", "Noelia"
    name_random = random.choice(name_random_names)
    return name_random

def apellidos_random():
    apellidos_random_names = "Pérez", "Carrasco", "Orozco", "Sallah", "Sánchez", "Abascal", "García", "Florea", "Tyson", "Martín", "Chia", "Fuentes", "Balboa", "Montalvo"
    apellidos_random = random.choice(apellidos_random_names)
    return apellidos_random

def telefono_random():
    telefono_random_numbers1 = random.randint(0,9)
    telefono_random_numbers2 = random.randint(0,9)
    telefono_random_numbers3 = random.randint(0,9)
    telefono_random_numbers4 = random.randint(0,9)
    telefono_random_numbers5 = random.randint(0,9)
    telefono_random_numbers6 = random.randint(0,9)
    telefono_random_numbers7 = random.randint(0,9)
    telefono_random_numbers8 = random.randint(0,9)
    telefono_random_numbers9 = random.randint(0,9)
    telefono_random = f'{telefono_random_numbers1}{telefono_random_numbers2}{telefono_random_numbers3} {telefono_random_numbers4}{telefono_random_numbers5} {telefono_random_numbers6}{telefono_random_numbers7} {telefono_random_numbers8}{telefono_random_numbers9}'
    return telefono_random
def clear_item():
    qty_spinbox.delete(0, tkinter.END)
    qty_spinbox.insert(0, "1")
    desc_entry.delete(0, tkinter.END)
    desc_entry.configure(placeholder_text=desc_random())
    price_spinbox.delete(0, tkinter.END)
    price_spinbox.insert(0, "0.0")

invoice_list = []

def add_item():
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    if desc:
        desc = desc_entry.get()
    else:
        desc = desc_entry._placeholder_text
    price  = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total]
    tree.insert('', 'end', values=invoice_item)
    clear_item()
    invoice_list.append(invoice_item)

def delete_item():
     for i in tree.selection():
         idx = tree.index(i)
         tree.delete(i)
         del invoice_list[idx]

def new_invoice():
    fn_entry.delete(0, tkinter.END)
    fn_entry.configure(placeholder_text=name_random())
    ln_entry.delete(0, tkinter.END)
    ln_entry.configure(placeholder_text=apellidos_random())
    phone_entry.delete(0, tkinter.END)
    phone_entry.configure(placeholder_text=telefono_random())
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate('Python/Invoice Generator/invoice_template.docx')
    fname = fn_entry.get()
    lname = ln_entry.get()
    phone = phone_entry.get()
    if fname:
        fname = fn_entry.get()
    else:
        fname = fn_entry._placeholder_text
    if lname:
        lname= ln_entry.get()
    else:
        lname = ln_entry._placeholder_text
    name = fname+f' {lname}'
    if phone:
        phone = phone_entry.get()
    else:
        phone = phone_entry._placeholder_text
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 0.1
    total = subtotal*(1-salestax)
    doc.render({"name": name,
                "phone": phone,
                "subtotal": subtotal,
                "salestax": str(salestax*100)+"%",
                "total": total,
                "invoice_list": invoice_list})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    messagebox.showinfo("Archivo guardado", "¡Archivo guardado con éxito!")
    new_invoice()
        

customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.title("Formulario para Generar la Factura")

frame = customtkinter.CTkFrame(app)
frame.pack(padx=20, pady=10)

fn_label = customtkinter.CTkLabel(frame, text="Nombre")
fn_label.grid(row=0, column=0, padx=10, pady=5)
ln_label= customtkinter.CTkLabel(frame, text="Apellido")
ln_label.grid(row=0, column=1, padx=10, pady=5)

fn_entry = customtkinter.CTkEntry(frame, placeholder_text=name_random())
ln_entry = customtkinter.CTkEntry(frame, placeholder_text=apellidos_random())
fn_entry.grid(row=1, column=0, padx=10, pady=5)
ln_entry.grid(row=1, column=1, padx=10, pady=5)

phone_label = customtkinter.CTkLabel(frame, text="Número de Teléfono")
phone_label.grid(row=0, column=2, padx=10, pady=5)
phone_entry = customtkinter.CTkEntry(frame, placeholder_text=telefono_random())
phone_entry.grid(row=1, column=2, padx=10, pady=5)

qty_label = customtkinter.CTkLabel(frame, text="Cantidad")
qty_label.grid(row=2, column=0, padx=10, pady=5)
qty_spinbox = tkinter.Spinbox(frame, from_=1, to=100)
qty_spinbox.grid(row=3, column=0, padx=10, pady=5)

desc_label = customtkinter.CTkLabel(frame, text="Descripción")
desc_label.grid(row=2, column=1, padx=10, pady=5)
desc_entry = customtkinter.CTkEntry(frame, placeholder_text=desc_random())
desc_entry.grid(row=3, column=1, padx=10, pady=5)

price_label = customtkinter.CTkLabel(frame, text="Precio de la Unidad")
price_label.grid(row=2, column=2, padx=10, pady=5)
price_spinbox = tkinter.Spinbox(frame, from_=0.0, to=500, increment=0.5)
price_spinbox.grid(row=3, column=2, padx=10, pady=5)

add_item_button = customtkinter.CTkButton(frame, command= add_item, text = "Añadir ítem", fg_color='#3e6bde', hover_color='#2e4fa3', border_color='#0f0000', border_width=1)
add_item_button.grid(row=4, column=1, padx=10, pady=5)
add_item_button = customtkinter.CTkButton(frame, command= delete_item, text = "Eliminar ítem", fg_color='#3e6bde', hover_color='#2e4fa3', border_color='#0f0000', border_width=1)
add_item_button.grid(row=4, column=2, padx=10, pady=5)

columns = ('cantidad', 'descripción', 'precio', 'total')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('cantidad', text="Cantidad")
tree.heading('descripción', text="Descripción")
tree.heading('precio', text="Precio")
tree.heading('total', text="Total")
tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

save_invoice_button = customtkinter.CTkButton(frame, command= generate_invoice, text = "Guardar factura", fg_color='#3e6bde', hover_color='#2e4fa3', border_color='#0f0000', border_width=1)
save_invoice_button.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)
new_invoice_button = customtkinter.CTkButton(frame, command= new_invoice, text = "Nueva factura", fg_color='#3e6bde', hover_color='#2e4fa3', border_color='#0f0000', border_width=1)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)
app.mainloop()