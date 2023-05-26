import pystray
from PIL import Image

def on_quit(icon, item):
    icon.stop()

# Ruta del archivo de imagen que deseas utilizar como ícono
icon_path = 'ruta_del_icono.png'

# Carga la imagen y crea el ícono
image = Image.open(icon_path)
icon = pystray.Icon("my_icon", image, "My Icon", menu=pystray.Menu())

# Agrega un elemento al menú de íconos para salir de la aplicación
icon.menu.add_item(pystray.MenuItem("Salir", on_quit))

# Inicia el ícono
icon.run()

