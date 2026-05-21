from PIL import Image
import os

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "icon.png")
img = Image.open(src).convert("RGBA")

# Various sizes for favicon and PWA
sizes = [
    ("favicon-16.png", 16),
    ("favicon-32.png", 32),
    ("favicon-48.png", 48),
    ("apple-touch-icon.png", 180),
    ("icon-192.png", 192),
    ("icon-512.png", 512),
]
for name, size in sizes:
    out = img.resize((size, size), Image.LANCZOS)
    out.save(os.path.join(base, name), optimize=True)
    print(f"  {name}: {size}x{size}")

# Multi-size ICO
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
img.save(os.path.join(base, "favicon.ico"), format="ICO", sizes=ico_sizes)
print(f"  favicon.ico: {ico_sizes}")

print("Done")
