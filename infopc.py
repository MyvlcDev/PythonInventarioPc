import socket
import platform
import psutil
import time
from datetime import datetime
import os

hostname = socket.gethostname()
os = platform.system()
version = platform.version()
arquitectura= platform.architecture()[0]
memoria = psutil.virtual_memory()
memoriaRamTotal = memoria.total /(1024**3) ## convertimos a GB
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dominio = socket.getfqdn()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

usuario=""
## placa base
pb_numeroserie=""
pb_modelo="" 
pb_fabricante=""

## red

dns_pri=""
dns_sec=""
puerta_enlace=""

## procesador

cores=""

## hd



print("Escribir en la base de datos\n\n")

print("")
print(f"Nombre del host: {hostname}")
print(f"Sistema operativo: {os}")
print(f"Versión: {version}")
print(f"Fecha actual: {date}")
print(f"Ariquitectura: {arquitectura}")
print("Plataforma:", platform.platform())
print("Núcleos físicos:", psutil.cpu_count(logical=False))
print("Núcleos lógicos:", psutil.cpu_count(logical=True))
print(f"Memoria: {memoria}")
print(f"Memoria Ram Total: {memoriaRamTotal} GB")
print(f"IP: {ip}")
print(f"Dominio: {dominio}")
##print(f"Usuario actual:", (str)os.getlogin())

print("Discoss Duros:")
disk_info = psutil.disk_partitions()
for partition in disk_info:
    print(f"Disco: {partition.device} - Tipo de sistema de archivos: {partition.fstype}")
    disk_usage = psutil.disk_usage(partition.mountpoint)
    print(f"  Espacio total: {disk_usage.total} - Espacio usado: {disk_usage.used} - Espacio libre: {disk_usage.free}")

print("\n")

