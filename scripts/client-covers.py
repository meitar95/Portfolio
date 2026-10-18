"""Rebuild the Sentrycs and Cybersixgill homepage covers on the same system as the two
Afimilk cards: flat brand field, the client's own logo on the left, a product window
bleeding off the right edge, and a couple of small brand accents."""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, sys
I='/home/claude/portfolio/public/images/'; S=sys.argv[1]
W,H=1600,900

def window(img, width, radius=20, bar=36):
    """Put a screenshot in a light browser chrome, returned with its rounded mask."""
    h=int(img.height*width/img.width); img=img.resize((width,h),Image.LANCZOS)
    win=Image.new('RGB',(width,h+bar),(255,255,255)); win.paste(img,(0,bar))
    d=ImageDraw.Draw(win); d.rectangle((0,0,width,bar),fill=(241,244,247))
    for i,c in enumerate([(255,95,87),(254,188,46),(40,200,64)]): d.ellipse((18+i*22,13,29+i*22,24),fill=c)
    mask=Image.new('L',win.size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,win.width,win.height+60),radius,fill=255)
    return win, mask

def place(cv, win, mask, x, y, shadow=(10,20,40)):
    sh=Image.new('L',(W,H),0)
    ImageDraw.Draw(sh).rounded_rectangle((x+8,y+28,x+win.width+40,y+win.height+40),26,fill=120)
    sh=sh.filter(ImageFilter.GaussianBlur(36))
    cv=Image.composite(Image.new('RGB',(W,H),shadow),cv,sh)
    cv.paste(win,(x,y),mask); return cv

def matte(arr, bg_pct=92):
    """Alpha matte for dark artwork sitting on a light, slightly uneven background."""
    lum=arr.sum(2)/3; bg=np.percentile(lum,bg_pct,axis=0)[None,:]
    return np.clip((bg-lum)/np.maximum(bg-12,1),0,1)

# ---------- Sentrycs: black-on-light wordmark, so the field stays light ----------
src=Image.open(I+'sentrycs-1600.webp').convert('RGB')
w=src.crop((44,735,450,822)); lum=w.convert('L')
bgl=lum.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(12))
Lv=np.array(lum).astype(float); Bv=np.array(bgl).astype(float)
al=np.clip((Bv-Lv)/np.maximum(Bv*0.78,1),0,1)
al=np.clip((al-0.42)/0.40,0,1)
al=Image.fromarray((al*255).astype('uint8')).filter(ImageFilter.MedianFilter(3))
word=Image.new('RGBA',w.size,(17,17,19,255)); word.putalpha(al)
ac=src.crop((176,620,320,706)); arr=np.array(ac).astype(int)
m=((arr[:,:,2]>150)&(arr[:,:,0]<150)&(arr[:,:,2]-arr[:,:,0]>45)).astype('uint8')*255
m=Image.fromarray(m).filter(ImageFilter.GaussianBlur(0.7))
arrows=Image.fromarray(np.dstack([np.array(ac).astype('uint8'),np.array(m)]),'RGBA')

cv=Image.new('RGB',(W,H),(240,242,246))
shot,mask=window(Image.open(I+'sentrycs/realtime-final-1600.webp').convert('RGB'),1120)
cv=place(cv,shot,mask,660,210,shadow=(96,108,128))
aw=168; a2=arrows.resize((aw,int(arrows.height*aw/arrows.width)),Image.LANCZOS)
cv.paste(a2,(112,318),a2)
ww=404; w2=word.resize((ww,int(word.height*ww/word.width)),Image.LANCZOS)
cv.paste(w2,(110,474),w2)
cv.save(S+'/sentrycs-cover.png')

# ---------- Cybersixgill: white logo already sits on their flat navy ----------
c=Image.open(I+'cybersixgill-1600.webp').convert('RGB')
logo=c.crop((45,742,395,858))  # logo + wordmark, background is flat #00265F
la=np.array(logo).astype(float); bg=np.array([0,38,95.])
alpha=np.clip(np.abs(la-bg).sum(2)/150,0,1)
logo_rgba=Image.fromarray(np.dstack([np.array(logo),(alpha*255).astype('uint8')]),'RGBA')
cv=Image.new('RGB',(W,H),(0,38,95))
shot,mask=window(Image.open(I+'cybersixgill/dashboard-1600.webp').convert('RGB'),1120)
cv=place(cv,shot,mask,660,210,shadow=(0,16,44))
lw=430; l2=logo_rgba.resize((lw,int(logo_rgba.height*lw/logo_rgba.width)),Image.LANCZOS)
cv.paste(l2,(110,int(H/2-l2.height/2)),l2)
cv.save(S+'/cybersixgill-cover.png')
