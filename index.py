import psutil
from tabulate import tabulate
from termcolor import colored

def get_process_info():
    process_info = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
            process_info.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_info

def get_cpu_usage():
    return psutil.cpu_percent(interval=1, percpu=True)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'percent': mem.percent
    }

def generate_report():
    process_info = get_process_info()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()

    report = colored("=== Informe del sistema ===", attrs=['bold']) + "\n\n"

    # Procesos en ejecución
    headers = ["PID", "Nombre", "Uso de CPU (%)", "Uso de memoria (%)"]
    process_data = []

    for proc in process_info:
        pid = proc['pid']
        name = proc['name']
        cpu_percent = proc['cpu_percent']
        memory_percent = proc['memory_percent']

        # Resaltar procesos con alto consumo en rojo y bajo consumo en verde
        if cpu_percent > 50 or memory_percent > 50:
            process_data.append([colored(pid, 'red'), colored(name, 'red'), colored(cpu_percent, 'red'), colored(memory_percent, 'red')])
        elif cpu_percent < 10 and memory_percent < 10:
            process_data.append([colored(pid, 'green'), colored(name, 'green'), colored(cpu_percent, 'green'), colored(memory_percent, 'green')])
        else:
            process_data.append([pid, name, cpu_percent, memory_percent])

    process_table = tabulate(process_data, headers, tablefmt="pipe")

    report += colored("--- Procesos en ejecución ---", attrs=['bold']) + "\n"
    report += process_table + "\n\n"

    # Uso de CPU
    cpu_data = []
    for i, cpu in enumerate(cpu_usage):
        if cpu > 50:
            cpu_data.append([colored(f"CPU {i}", 'red'), colored(cpu, 'red')])
        elif cpu < 10:
            cpu_data.append([colored(f"CPU {i}", 'green'), colored(cpu, 'green')])
        else:
            cpu_data.append([f"CPU {i}", cpu])

    cpu_table = tabulate(cpu_data, headers=["CPU", "Uso (%)"], tablefmt="pipe")

    report += colored("--- Uso de CPU ---", attrs=['bold']) + "\n"
    report += cpu_table + "\n\n"

    # Uso de memoria
    memory_data = [
        ["Total", convert_size(memory_usage['total'])],
        ["Disponible", convert_size(memory_usage['available'])],
        ["Utilizado", convert_size(memory_usage['used'])],
        ["Porcentaje de uso", f"{memory_usage['percent']}%"]
    ]
    memory_table = tabulate(memory_data, headers=["Tipo", "Valor"], tablefmt="pipe")

    report += colored("--- Uso de memoria ---", attrs=['bold']) + "\n"
    report += memory_table + "\n"

    return report

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    size = round(size_bytes / p, 2)
    return f"{size} {size_names[i]}"

if __name__ == "__main__":
    import math
    report = generate_report()
    print(report)
