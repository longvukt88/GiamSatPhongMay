from flask import Flask, request, jsonify
import time

app = Flask(__name__)
du_lieu_cac_may = {}

NGUONG_CPU = 80
NGUONG_RAM = 80
NGUONG_DISK = 90

@app.route("/gui", methods=["POST"])
def nhan_so_lieu():
    data = request.get_json()
    data["lan_cuoi"] = time.time()
    du_lieu_cac_may[data["ten_may"]] = data
    return jsonify({"ket_qua": "ok"})

@app.route("/api/may")
def api_may():
    return jsonify({
        "nguong": {"cpu": NGUONG_CPU, "ram": NGUONG_RAM, "disk": NGUONG_DISK},
        "bay_gio": time.time(),
        "may": list(du_lieu_cac_may.values()),
    })

TRANG = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Giám sát phòng máy</title>
<style>
  body { font-family: Arial, sans-serif; margin: 24px; background: #f4f6f8; }
  h1 { color: #1a3c6e; }
  table { border-collapse: collapse; width: 100%; background: white; }
  th, td { border: 1px solid #ccc; padding: 10px; text-align: center; }
  th { background: #1a3c6e; color: white; }
  .bt { background: #d9f2d9; }
  .cao { background: #ffb3b3; font-weight: bold; }
  .mat { color: #999; background: #eee; }
</style>
</head>
<body>
<h1>Giám sát phòng máy</h1>
<p id="tong">Đang tải...</p>
<table>
  <thead>
    <tr><th>Tên máy</th><th>CPU (%)</th><th>RAM (%)</th><th>Ổ đĩa (%)</th><th>Trạng thái</th></tr>
  </thead>
  <tbody id="bang"></tbody>
</table>

<script>
async function capNhat() {
  try {
    const res = await fetch("/api/may");
    const d = await res.json();
    let html = "";
    let soCanhBao = 0;
    for (const m of d.may) {
      const matKetNoi = (d.bay_gio - m.lan_cuoi) > 15;
      const cpuCao = m.cpu >= d.nguong.cpu;
      const ramCao = m.ram >= d.nguong.ram;
      const diskCao = m.disk >= d.nguong.disk;
      let tt = "Bình thường";
      if (matKetNoi) tt = "Mất kết nối";
      else if (cpuCao || ramCao || diskCao) { tt = "Cảnh báo"; soCanhBao++; }
      html += "<tr" + (matKetNoi ? ' class="mat"' : "") + ">" +
        "<td>" + m.ten_may + "</td>" +
        "<td class='" + (cpuCao ? "cao" : "bt") + "'>" + m.cpu + "</td>" +
        "<td class='" + (ramCao ? "cao" : "bt") + "'>" + m.ram + "</td>" +
        "<td class='" + (diskCao ? "cao" : "bt") + "'>" + m.disk + "</td>" +
        "<td>" + tt + "</td></tr>";
    }
    document.getElementById("bang").innerHTML = html;
    document.getElementById("tong").textContent =
      "Số máy: " + d.may.length + " | Đang cảnh báo: " + soCanhBao +
      " | Cập nhật: " + new Date().toLocaleTimeString("vi-VN");
  } catch (e) {
    document.getElementById("tong").textContent = "Không kết nối được máy chủ";
  }
}
capNhat();
setInterval(capNhat, 5000);
</script>
</body>
</html>
"""

@app.route("/")
def trang_chu():
    return TRANG

app.run(host="0.0.0.0", port=5000)