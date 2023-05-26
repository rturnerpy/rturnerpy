import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

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

def deshacer():
    text_editor.edit_undo()

def rehacer():
    text_editor.edit_redo()

def copiar():
    text_editor.event_generate("<<Copy>>")

def cortar():
    text_editor.event_generate("<<Cut>>")

def pegar():
    text_editor.event_generate("<<Paste>>")

def seleccionar_todo():
    text_editor.tag_add(tk.SEL, "1.0", tk.END)

def buscar():
    ventana_buscar = tk.Toplevel(root)
    ventana_buscar.title("Buscar")
    etiqueta_buscar = ttk.Label(ventana_buscar, text="Buscar:")
    etiqueta_buscar.pack(side=tk.LEFT, padx=5, pady=5)
    entrada_buscar = ttk.Entry(ventana_buscar, width=30)
    entrada_buscar.pack(side=tk.LEFT, padx=5, pady=5)
    boton_buscar = ttk.Button(ventana_buscar, text="Buscar", command=lambda: buscar_texto(entrada_buscar.get()))
    boton_buscar.pack(side=tk.LEFT, padx=5, pady=5)

def buscar_texto(texto):
    posicion = text_editor.search(texto, "1.0", stopindex=tk.END)
    if posicion:
        inicio = posicion
        fin = f"{posicion}+{len(texto)}c"
        text_editor.tag_remove(tk.SEL, "1.0", tk.END)
        text_editor.tag_add(tk.SEL, inicio, fin)
        text_editor.mark_set(tk.INSERT, inicio)
        text_editor.see(tk.INSERT)

def reemplazar():
    ventana_reemplazar = tk.Toplevel(root)
    ventana_reemplazar.title("Reemplazar")
    etiqueta_buscar = ttk.Label(ventana_reemplazar, text="Buscar:")
    etiqueta_buscar.pack(side=tk.TOP, padx=5, pady=5)
    entrada_buscar = ttk.Entry(ventana_reemplazar, width=30)
    entrada_buscar.pack(side=tk.TOP, padx=5, pady=5)
    etiqueta_reemplazar = ttk.Label(ventana_reemplazar, text="Reemplazar con:")
    etiqueta_reemplazar.pack(side=tk.TOP, padx=5, pady=5)
    entrada_reemplazar = ttk.Entry(ventana_reemplazar, width=30)
    entrada_reemplazar.pack(side=tk.TOP, padx=5, pady=5)
    boton_reemplazar = ttk.Button(ventana_reemplazar, text="Reemplazar", command=lambda: reemplazar_texto(entrada_buscar.get(), entrada_reemplazar.get()))
    boton_reemplazar.pack(side=tk.TOP, padx=5, pady=5)

def reemplazar_texto(texto_buscar, texto_reemplazar):
    contenido = text_editor.get("1.0", tk.END)
    contenido_modificado = contenido.replace(texto_buscar, texto_reemplazar)
    text_editor.delete("1.0", tk.END)
    text_editor.insert(tk.END, contenido_modificado)

def contar_palabras():
    contenido = text_editor.get("1.0", tk.END)
    palabras = contenido.split()
    cantidad_palabras = len(palabras)
    messagebox.showinfo("Contador de Palabras", f"Cantidad de palabras: {cantidad_palabras}")

def cambiar_tamano_fuente(delta):
    actual = text_editor['font'].split()[1]
    nuevo_tamano = int(actual) + delta
    text_editor.configure(font=(None, nuevo_tamano))

def menu():
    menu_bar = tk.Menu(root)

    archivo_menu = tk.Menu(menu_bar, tearoff=0)
    archivo_menu.add_command(label="Abrir", command=abrir_archivo)
    archivo_menu.add_command(label="Guardar", command=guardar_archivo)
    archivo_menu.add_separator()
    archivo_menu.add_command(label="Salir", command=root.quit)
    menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

    editar_menu = tk.Menu(menu_bar, tearoff=0)
    editar_menu.add_command(label="Deshacer", command=deshacer)
    editar_menu.add_command(label="Rehacer", command=rehacer)
    editar_menu.add_separator()
    editar_menu.add_command(label="Copiar", command=copiar)
    editar_menu.add_command(label="Cortar", command=cortar)
    editar_menu.add_command(label="Pegar", command=pegar)
    editar_menu.add_separator()
    editar_menu.add_command(label="Seleccionar Todo", command=seleccionar_todo)
    menu_bar.add_cascade(label="Editar", menu=editar_menu)

    buscar_menu = tk.Menu(menu_bar, tearoff=0)
    buscar_menu.add_command(label="Buscar", command=buscar)
    buscar_menu.add_command(label="Reemplazar", command=reemplazar)
    menu_bar.add_cascade(label="Buscar", menu=buscar_menu)

    herramientas_menu = tk.Menu(menu_bar, tearoff=0)
    herramientas_menu.add_command(label="Contar Palabras", command=contar_palabras)
    menu_bar.add_cascade(label="Herramientas", menu=herramientas_menu)

    tamano_fuente_menu = tk.Menu(menu_bar, tearoff=0)
    tamano_fuente_menu.add_command(label="Aumentar", command=lambda: cambiar_tamano_fuente(2))
    tamano_fuente_menu.add_command(label="Disminuir", command=lambda: cambiar_tamano_fuente(-2))
    menu_bar.add_cascade(label="Tamaño de Fuente", menu=tamano_fuente_menu)

    root.config(menu=menu_bar)

root = tk.Tk()
root.title("Editor de Textos")

style = ttk.Style()
style.theme_use("clam")  # Puedes probar diferentes temas: "clam", "alt", "default", "vista"

text_editor = tk.Text(root)
text_editor.pack(fill=tk.BOTH, expand=True)

menu()

root.mainloop()
