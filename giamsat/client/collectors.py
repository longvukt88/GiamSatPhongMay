import psutil
from common.models import SystemStats

class SystemCollector:
    """Đọc CPU, RAM, ổ đĩa của máy hiện tại."""

    def __init__(self, o_dia="/"):
        self.o_dia = o_dia

    def collect(self) -> SystemStats:
        return SystemStats(
            cpu=psutil.cpu_percent(interval=1),
            ram=psutil.virtual_memory().percent,
            disk=psutil.disk_usage(self.o_dia).percent,
        )