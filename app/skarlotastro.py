import tkinter as tk
from tkinter import filedialog, messagebox

def abrir_archivo():
    nombre_archivo = filedialog.askopenfilename(filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if nombre_archivo:
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
            text_editor.delete("1.0", tk.END)
            text_editor.insert(tk.END, contenido)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no existe.")

def guardar_archivo():
    contenido = text_editor.get("1.0", tk.END)
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if nombre_archivo:
        try:
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(contenido)
            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
        except:
            messagebox.showerror("Error", "Error al guardar el archivo.")

def menu():
    menu_bar = tk.Menu(root)

    archivo_menu = tk.Menu(menu_bar, tearoff=0)
    archivo_menu.add_command(label="Abrir", command=abrir_archivo)
    archivo_menu.add_command(label="Guardar", command=guardar_archivo)
    archivo_menu.add_separator()
    archivo_menu.add_command(label="Salir", command=root.quit)
    menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

    root.config(menu=menu_bar)

root = tk.Tk()
root.title("Editor de Textos")

text_editor = tk.Text(root)
text_editor.pack(fill=tk.BOTH, expand=True)

menu()

root.mainloop()
