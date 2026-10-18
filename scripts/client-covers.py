"""Rebuild the Sentrycs and Cybersixgill homepage covers on the same system as the two
Afimilk cards: a flat field in the client's own color, their official logo on the left,
a product window bleeding off the right edge, and a soft shadow.

Logos come from the brand PNGs in scripts/assets/ (supplied by the client, transparent,
already trimmed to their artwork). Run from the repo root:

    python3 scripts/client-covers.py
"""
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'public' / 'images'
LOGO = Path(__file__).resolve().parent / 'assets'
W, H = 1600, 900
SCREEN_H = 616        # one window height across every cover


def window(shot, screen_h, radius=20, bar=36):
    """Put a screenshot in a light browser chrome; returns the image and its rounded mask.

    Sized by HEIGHT, not width, so every cover's window is exactly the same height no matter
    the screenshot's aspect ratio. The extra width just runs further off the right edge."""
    width = int(shot.width * screen_h / shot.height)
    shot = shot.resize((width, screen_h), Image.LANCZOS)
    h = screen_h
    win = Image.new('RGB', (width, h + bar), (255, 255, 255))
    win.paste(shot, (0, bar))
    d = ImageDraw.Draw(win)
    d.rectangle((0, 0, width, bar), fill=(241, 244, 247))
    for i, c in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
        d.ellipse((18 + i * 22, 13, 29 + i * 22, 24), fill=c)
    mask = Image.new('L', win.size, 0)
    # The mask runs past the bottom so the window bleeds off the cover instead of ending in a curve
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, win.width, win.height + 60), radius, fill=255)
    return win, mask


def place(cv, win, mask, x, y, shadow):
    sh = Image.new('L', (W, H), 0)
    ImageDraw.Draw(sh).rounded_rectangle((x + 8, y + 28, x + win.width + 40, y + win.height + 40), 26, fill=120)
    sh = sh.filter(ImageFilter.GaussianBlur(36))
    cv = Image.composite(Image.new('RGB', (W, H), shadow), cv, sh)
    cv.paste(win, (x, y), mask)
    return cv


def put_logo(cv, path, width, x, cy):
    logo = Image.open(path).convert('RGBA')
    logo = logo.resize((width, int(logo.height * width / logo.width)), Image.LANCZOS)
    cv.paste(logo, (x, int(cy - logo.height / 2)), logo)


def build(bg, shot_path, logo_name, logo_width, logo_x, logo_cy, shadow, out):
    cv = Image.new('RGB', (W, H), bg)
    win, mask = window(Image.open(shot_path).convert('RGB'), SCREEN_H)
    cv = place(cv, win, mask, 760, 210, shadow)
    put_logo(cv, LOGO / logo_name, logo_width, logo_x, logo_cy)
    cv.save(IMG / f'{out}-1600.webp', quality=86)
    cv.resize((800, 450), Image.LANCZOS).save(IMG / f'{out}-800.webp', quality=86)
    print('wrote', out)


# Sentrycs: the wordmark is black, so the field stays light. Vertical lockup, mark over word.
build((240, 242, 246), IMG / 'sentrycs' / 'realtime-final-1600.webp',
      'sentrycs-logo.png', 300, 112, 450, (96, 108, 128), 'sentrycs')

# Cybersixgill: white wordmark on their own navy. Horizontal lockup.
build((0, 38, 95), IMG / 'cybersixgill' / 'dashboard-1600.webp',
      'cybersixgill-logo.png', 440, 108, 450, (0, 16, 44), 'cybersixgill')
