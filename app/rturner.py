import os

def resetear_ordenador():
    # Comando para borrar todos los datos del disco
    comando_borrado = "sudo dd if=/dev/zero of=/dev/sda bs=1M count=10"
    
    # Comando para reinstalar Ubuntu desde un medio de instalación
    comando_instalacion = "sudo /usr/bin/env bash -c 'apt-get install -y --reinstall ubuntu-desktop'"
    
    # Comando para reiniciar el ordenador
    comando_reinicio = "sudo reboot"
    
    # Preguntar al usuario si desea continuar
    confirmacion = input("Este proceso borrará todos los datos de tu disco y restablecerá el ordenador a su estado de fábrica. ¿Estás seguro de que deseas continuar? (s/n): ")
    
    if confirmacion.lower() == 's':
        # Ejecutar el comando de borrado
        os.system(comando_borrado)
        
        # Ejecutar el comando de reinstalación
        os.system(comando_instalacion)
        
        # Preguntar al usuario si desea reiniciar el ordenador
        confirmacion_reinicio = input("El proceso de reinicio se ha completado. ¿Deseas reiniciar el ordenador ahora? (s/n): ")
        
        if confirmacion_reinicio.lower() == 's':
            # Reiniciar el ordenador
            os.system(comando_reinicio)
        else:
            print("El reinicio se ha omitido. Puedes reiniciar manualmente cuando estés listo.")
    else:
        print("El proceso ha sido cancelado. No se realizarán cambios en el ordenador.")

# Llamada a la función para resetear el ordenador
resetear_ordenador()
