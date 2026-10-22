from common.models import SystemStats, Machine

m = Machine(ten_may="MAY01", stats=SystemStats(cpu=10, ram=70, disk=24))
print(m)
print("Mất kết nối?", m.mat_ket_noi())