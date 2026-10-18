from PIL import Image, ImageDraw, ImageFilter
import numpy as np, sys
I='/home/claude/portfolio/public/images/'; S=sys.argv[1]
far=Image.open(I+'farmers-1600.webp').convert('RGB')
c=far.crop((40,200,720,380)); a=np.array(c).astype(int); m=(a.sum(2)>660); ys,xs=np.where(m)
logo=c.crop((xs.min()-3,ys.min()-3,xs.max()+4,ys.max()+4))
la=np.array(logo).astype(float); bgc=np.array([40,123,172.])
alpha=np.clip((la-bgc).sum(2)/((255-bgc).sum()),0,1)
L=Image.new('RGBA',logo.size,(255,255,255,0)); L.putalpha(Image.fromarray((alpha*255).astype('uint8')))
W,H=1600,900; BG=(40,123,172)
cv=Image.new('RGB',(W,H),BG)
glow=Image.new('L',(W,H),0); ImageDraw.Draw(glow).ellipse((600,0,1900,1100),fill=70); glow=glow.filter(ImageFilter.GaussianBlur(180))

lw=606; L2=L.resize((lw,int(L.height*lw/L.width)),Image.LANCZOS)
cv.paste(L2,(76,226),L2)  # same spot and size as the Farmers cover
dash=Image.open(S+'/figma-tasks.png').convert('RGB')
ww=1100; dh=int(dash.height*ww/dash.width); dash=dash.resize((ww,dh),Image.LANCZOS)
bar=36; win=Image.new('RGB',(ww,dh+bar),(255,255,255)); win.paste(dash,(0,bar))
wd=ImageDraw.Draw(win); wd.rectangle((0,0,ww,bar),fill=(241,244,247))
for i,col in enumerate([(255,95,87),(254,188,46),(40,200,64)]): wd.ellipse((18+i*22,13,29+i*22,24),fill=col)
mask=Image.new('L',win.size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,win.width,win.height+40),20,fill=255)
x,y=760,230
sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rounded_rectangle((x+6,y+26,x+ww+40,y+win.height+40),24,fill=130); sh=sh.filter(ImageFilter.GaussianBlur(36))
cv=Image.composite(Image.new('RGB',(W,H),(14,52,84)),cv,sh)
cv.paste(win,(x,y),mask)
# Brand stars lifted straight from Afimilk's own artwork (gold from the Farmers cover,
# light blue from the original herd cover), keyed off the flat blue so they paste cleanly.
def lift(path,box,col):
    src=np.array(Image.open(path).convert('RGB').crop(box)).astype(float)
    bgc=np.array([40,123,172.]); colv=np.array(col,float)
    a=np.clip(((src-bgc)*(colv-bgc)).sum(2)/((colv-bgc)**2).sum(),0,1)
    t=Image.new('RGBA',(src.shape[1],src.shape[0]),tuple(col)+(0,)); t.putalpha(Image.fromarray((a*255).astype('uint8'))); return t
def put(t,cx,cy,sc=1.0):
    if sc!=1.0: t=t.resize((int(t.width*sc),int(t.height*sc)),Image.LANCZOS)
    cv.paste(t,(int(cx-t.width/2),int(cy-t.height/2)),t)
gold=lift(I+'farmers-1600.webp',(414,522,452,560),(252,176,13))
blue=lift(S+'/old-herd.webp',(525,510,575,555),(75,214,244))
put(gold,62,214,1.15); put(blue,650,470,0.9)
cv.save(S+'/herd-cover-new.png')
