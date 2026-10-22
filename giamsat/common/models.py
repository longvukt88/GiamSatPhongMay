from dataclasses import dataclass, field
import time

@dataclass
class SystemStats:
    cpu: float
    ram: float
    disk: float

@dataclass
class WindowInfo:
    title: str
    process: str
    pid: int

@dataclass
class Machine:
    ten_may: str
    stats: SystemStats | None = None
    windows: list[WindowInfo] = field(default_factory=list)
    lan_cuoi: float = field(default_factory=time.time)

    def mat_ket_noi(self, quang=15) -> bool:
        return time.time() - self.lan_cuoi > quang