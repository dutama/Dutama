"""Membuat ikon aplikasi dari logo DUTAMA yang ada di index.html."""
import re, base64, io, os, shutil
from PIL import Image

src = open("index.html", encoding="utf-8").read()
m = re.search(r"data:image/png;base64,([A-Za-z0-9+/=]+)", src)
logo = Image.open(io.BytesIO(base64.b64decode(m.group(1)))).convert("RGBA")
res = "android/app/src/main/res"
shutil.rmtree(os.path.join(res, "mipmap-anydpi-v26"), ignore_errors=True)  # pakai ikon PNG di semua versi
for d, px in {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}.items():
    canvas = Image.new("RGBA", (px, px), (255, 255, 255, 255))
    h = int(px * 0.78); w = int(logo.width * h / logo.height)
    canvas.paste(logo.resize((w, h), Image.LANCZOS), ((px - w) // 2, (px - h) // 2))
    folder = os.path.join(res, "mipmap-" + d)
    os.makedirs(folder, exist_ok=True)
    for n in ("ic_launcher.png", "ic_launcher_round.png", "ic_launcher_foreground.png"):
        canvas.convert("RGB").save(os.path.join(folder, n))
print("Ikon dibuat")
