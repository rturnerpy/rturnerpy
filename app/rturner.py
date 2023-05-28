import os

def resetear_ordenador(idioma):
    # Comando para borrar todos los datos del disco
    comando_borrado = "sudo dd if=/dev/zero of=/dev/sda bs=1M count=-1"
    
    # Comando para reinstalar Ubuntu desde un medio de instalación
    comando_instalacion = "sudo /usr/bin/env bash -c 'apt-get install -y --reinstall ubuntu-desktop'"
    
    # Comando para reiniciar el ordenador
    comando_reinicio = "sudo reboot"
    
    if idioma.lower() == '1':
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
    elif idioma.lower() == '2':
        # Ask the user if they want to continue
        confirmation = input("This process will erase all data on your disk and reset the computer to its factory state. Are you sure you want to continue? (y/n): ")
    
        if confirmation.lower() == 'y':
            # Execute the wipe command
            os.system(comando_borrado)
            
            # Execute the reinstallation command
            os.system(comando_instalacion)
            
            # Ask the user if they want to restart the computer
            restart_confirmation = input("The reset process has completed. Do you want to restart the computer now? (y/n): ")
            
            if restart_confirmation.lower() == 'y':
                # Restart the computer
                os.system(comando_reinicio)
            else:
                print("The restart has been skipped. You can manually restart when you're ready.")
        else:
            print("The process has been canceled. No changes will be made to the computer.")
    else:
        print("Invalid language. Please select 'español' or 'english'.")

def seleccionar_idioma():
    idioma = input("Seleccione el idioma del programa | español (1) / inglés (2): ")
    return idioma

# Obtener el idioma seleccionado
idioma_seleccionado = seleccionar_idioma()

# Llamada a la función para resetear el ordenador
resetear_ordenador(idioma_seleccionado)
