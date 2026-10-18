"""Rebuild the two Afimilk homepage covers (Farmers app, Herd platform) as a matched pair.

Both sit on Afimilk's flat brand blue with the logo in the same spot and size, their own
two brand stars, and the product on the right running off the edge: phone renders for the
field app, a browser window for the herd platform. Everything is lifted from Afimilk's own
artwork, so no logo or star is redrawn. Run from the repo root:

    python3 scripts/afimilk-covers.py
"""
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'public' / 'images'
W, H = 1600, 900
BG = (40, 123, 172)          # Afimilk brand blue, sampled from their own artwork
GOLD = (252, 176, 13)
CYAN = (75, 214, 244)

brand = Image.open(IMG / 'farmers-1600.webp').convert('RGB')   # Afimilk's marketing render
herd_art = Image.open(ROOT / 'scripts' / 'assets' / 'afimilk-herd-art.webp').convert('RGB')


def lift(img, box, colour):
    """Pull one piece of flat artwork off the brand blue as a transparent layer."""
    s = np.array(img.crop(box)).astype(float)
    c, b = np.array(colour, float), np.array(BG, float)
    a = np.clip(((s - b) * (c - b)).sum(2) / ((c - b) ** 2).sum(), 0, 1)
    out = Image.new('RGBA', (s.shape[1], s.shape[0]), tuple(colour) + (0,))
    out.putalpha(Image.fromarray((a * 255).astype('uint8')))
    return out


def centre(cv, layer, cx, cy, scale=1.0):
    if scale != 1.0:
        layer = layer.resize((int(layer.width * scale), int(layer.height * scale)), Image.LANCZOS)
    cv.paste(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)), layer)


def logo_layer():
    crop = brand.crop((60, 210, 700, 360))
    a = np.array(crop).astype(float)
    alpha = np.clip((a - np.array(BG, float)).sum(2) / ((255 - np.array(BG)).sum()), 0, 1)
    out = Image.new('RGBA', crop.size, (255, 255, 255, 0))
    out.putalpha(Image.fromarray((alpha * 255).astype('uint8')))
    return out.crop(out.getbbox())


def base():
    """Flat field, logo and the two brand stars, identical on both covers."""
    cv = Image.new('RGB', (W, H), BG)
    logo = logo_layer()
    lw = 606
    cv.paste(logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS), (76, 226), logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS))
    centre(cv, lift(brand, (414, 522, 452, 560), GOLD), 62, 214, 1.15)
    centre(cv, lift(herd_art, (525, 510, 575, 555), CYAN), 650, 470, 0.9)
    return cv


# ---- Farmers: the phone renders, copied straight off the same flat blue ----
cv = base()
phones = brand.crop((840, 10, 1460, 890))
cv.paste(phones, (W - phones.width + 130, 8))
cv.save(IMG / 'farmers-1600.webp', quality=86)
cv.resize((800, 450), Image.LANCZOS).save(IMG / 'farmers-800.webp', quality=86)
print('wrote farmers')

# ---- Herd: the Daily Tasks screen in a browser window ----
cv = base()
shot = Image.open(ROOT / 'scripts' / 'assets' / 'herd-daily-tasks.png').convert('RGB')
ww, bar = 1100, 36
shot = shot.resize((ww, int(shot.height * ww / shot.width)), Image.LANCZOS)
win = Image.new('RGB', (ww, shot.height + bar), (255, 255, 255))
win.paste(shot, (0, bar))
d = ImageDraw.Draw(win)
d.rectangle((0, 0, ww, bar), fill=(241, 244, 247))
for i, c in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
    d.ellipse((18 + i * 22, 13, 29 + i * 22, 24), fill=c)
mask = Image.new('L', win.size, 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, win.width, win.height + 60), 20, fill=255)
x, y = 760, 230
sh = Image.new('L', (W, H), 0)
ImageDraw.Draw(sh).rounded_rectangle((x + 6, y + 26, x + ww + 40, y + win.height + 40), 24, fill=130)
sh = sh.filter(ImageFilter.GaussianBlur(36))
cv = Image.composite(Image.new('RGB', (W, H), (14, 52, 84)), cv, sh)
cv.paste(win, (x, y), mask)
cv.save(IMG / 'herd-1600.webp', quality=86)
cv.resize((800, 450), Image.LANCZOS).save(IMG / 'herd-800.webp', quality=86)
print('wrote herd')
