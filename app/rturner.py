import psutil
import platform
import time
from tabulate import tabulate
from termcolor import colored
import math

def get_process_info():
    process_info = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
            process_info.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_info

def get_memory_usage():
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'percent': mem.percent
    }

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    size = round(size_bytes / p, 2)
    return f"{size} {size_names[i]}"

while True:
    # Obtener los procesos
    process_info = get_process_info()

    # Mostrar los procesos
    headers = ["PID", "Nombre", "Uso de CPU (%)", "Uso de memoria (%)"]
    process_data = []

    for i, proc in enumerate(process_info):
        pid = proc['pid']
        name = proc['name']
        cpu_percent = proc['cpu_percent']
        memory_percent = proc['memory_percent']

        if cpu_percent > 50 or memory_percent > 50:
            process_data.append([colored(pid, 'red'), colored(name, 'red'), colored(cpu_percent, 'red'), colored(memory_percent, 'red')])
        elif cpu_percent < 10 and memory_percent < 10:
            process_data.append([colored(pid, 'green'), colored(name, 'green'), colored(cpu_percent, 'green'), colored(memory_percent, 'green')])
        else:
            process_data.append([pid, name, cpu_percent, memory_percent])

    process_table = tabulate(process_data, headers, tablefmt="pipe")
    print("\n=== Informe del sistema ===")
    print("\n--- Procesos en ejecución ---")
    print(process_table)

    # Obtener el uso de memoria
    memory_usage = get_memory_usage()

    # Mostrar el uso de memoria
    memory_data = [
        ["Total", convert_size(memory_usage['total'])],
        ["Disponible", convert_size(memory_usage['available'])],
        ["Utilizado", convert_size(memory_usage['used'])],
        ["Porcentaje de uso", f"{memory_usage['percent']}%"]
    ]
    memory_table = tabulate(memory_data, headers=["Tipo", "Valor"], tablefmt="pipe")
    print("\n--- Uso de memoria ---")
    print(memory_table)

    time.sleep(1)  # Esperar 1 segundo antes de actualizar la información nuevamente
