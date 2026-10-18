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


def phone(src, height, pad=15, radius=50):
    """A device frame in the same light chrome as the browser windows on the other covers."""
    sh = Image.open(src).convert('RGB')
    sh = sh.resize((int(sh.width * height / sh.height), height), Image.LANCZOS)
    fr = Image.new('RGBA', (sh.width + pad * 2, height + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(fr).rounded_rectangle((0, 0, fr.width - 1, fr.height - 1), radius, fill=(241, 244, 247, 255))
    m = Image.new('L', sh.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, sh.width - 1, sh.height - 1), radius - pad, fill=255)
    fr.paste(sh, (pad, pad), m)
    return fr


def drop(cv, layer, x, y, blur=34, strength=120):
    sh = Image.new('L', (W, H), 0)
    sh.paste(layer.split()[3].point(lambda v: strength if v > 8 else 0), (x + 6, y + 22))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    cv = Image.composite(Image.new('RGB', (W, H), (12, 48, 78)), cv, sh)
    cv.paste(layer, (x, y), layer)
    return cv


# ---- Farmers: one app screen, running off the right and bottom like the windows ----
cv = base()
cv = drop(cv, phone(ROOT / 'scripts' / 'assets' / 'farmers-tasks.png', 860), 1230, 150)
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
