import psutil
import requests
import socket
import time

DIA_CHI_MAY_CHU = "http://127.0.0.1:5000/gui"
TEN_MAY = socket.gethostname()

def doc_so_lieu():
    return {
        "ten_may": TEN_MAY,
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }

while True:
    du_lieu = doc_so_lieu()
    try:
        requests.post(DIA_CHI_MAY_CHU, json=du_lieu, timeout=3)
        print("Đã gửi:", du_lieu)
    except requests.exceptions.RequestException:
        print("Không gửi được, sẽ thử lại sau 5 giây")
    time.sleep(5)