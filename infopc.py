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


print("Escribir en la base de datos\n\n")


print(f"Nombre del host: {hostname}")
print(f"Sistema operativo: {os}")
print(f"Versión: {version}")
print(f"Fecha actual: {date}")
print(f"Ariquitectura: {arquitectura}")
print(f"Memoria: {memoria}")
print(f"Memoria Ram Total: {memoriaRamTotal} GB")
print(f"IP: {ip}")
print(f"Dominio: {dominio}")
print("\n\n")






