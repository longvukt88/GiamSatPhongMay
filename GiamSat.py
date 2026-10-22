import psutil
import time
from datetime import datetime
NGUONG_CPU =70
NGUONG_RAM =70
NGUONG_DISK =70
with open("nhatky.csv", "w", encoding="utf-8") as f:
    f.write("thoi_gian,cpu,ram,o_dia\n")
while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print("CPU:", cpu_percent, "%")
    print("RAM:", ram.percent, "%")
    print("Ổ đĩa:", disk.percent, "%")

    if ram.percent >= NGUONG_RAM:
        print("Cảnh báo: RAM đang sử dụng quá mức!")
    else:
        print("RAM dùng ở mức bình thường")

    if cpu_percent >= NGUONG_CPU:
        print("Cảnh báo: CPU đang sử dụng quá mức!")
    else:
        print("CPU dùng ở mức bình thường")

    if disk.percent >= NGUONG_DISK:
        print("Cảnh báo: Ổ đĩa đang sử dụng quá mức!")  
    else:
        print("Ổ đĩa dùng ở mức bình thường")

    time.sleep(5)

    bay_gio = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("nhatky.csv", "a", encoding="utf-8") as f:
        f.write(f"{bay_gio},{cpu_percent},{ram.percent},{disk.percent}\n")
