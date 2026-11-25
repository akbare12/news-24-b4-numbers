from PIL import Image, ImageDraw, ImageFont
import os
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; SANS="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SANSB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
def fb(s): return F(SANSB,s)
def fs(s): return F(SANS,s)
def fser(s): return F(SERIF,s)
def wrap(d,t,f,w):
    ls=[]; cur=""
    for wd in t.split():
        x=(cur+" "+wd).strip()
        if d.textlength(x,font=f)<=w: cur=x
        else:
            if cur: ls.append(cur)
            cur=wd
    if cur: ls.append(cur)
    return ls
def lines(d,x,y,ts,f,w,mx,fill,lh):
    n=0
    for ln in wrap(d,ts,f,w)[:mx]:
        d.text((x,y+n*lh),ln,font=f,fill=fill); n+=1
    return y+n*lh
def chip(d,x,y,s,c):
    f=fb(7); w=int(d.textlength(s,font=f))+9; d.rounded_rectangle([x,y,x+w,y+11],2,fill=c); d.text((x+4,y+1),s,font=f,fill=(255,255,255)); return w
def scene(d,x,y,w,h,k):
    _ox,_oy,_ow,_oh=x,y,w,h; _tmp=Image.new("RGB",(int(w),92),(226,232,240)); d=ImageDraw.Draw(_tmp); x=0; y=0; h=92
    d.rectangle([x,y,x+w,y+h],fill=(226,232,240))
    if k=="tower":
        d.rectangle([x,y+h,x+w,y+h],fill=(30,30,46)); d.rectangle([x+w*0.42,y+18,x+w*0.58,y+h],fill=(40,52,80)); d.rectangle([x+w*0.36,y+6,x+w*0.64,y+20],fill=(60,72,110)); d.polygon([(x+w*0.50,y),(x+w*0.44,y+10),(x+w*0.56,y+10)],fill=(178,34,34))
        for i in range(6): d.rectangle([x+w*0.44,y+24+i*10,x+w*0.56,y+30+i*10],fill=(255,210,90))
        d.ellipse([x+w*0.62,y+14,x+w*0.78,y+30],fill=(255,120,40)); d.ellipse([x+w*0.66,y+18,x+w*0.74,y+26],fill=(255,200,60)); d.polygon([(x+w*0.10,y+34),(x+w*0.22,y+28),(x+w*0.34,y+34)],fill=(90,90,90)); d.polygon([(x+w*0.10,y+30),(x+w*0.22,y+24),(x+w*0.34,y+30)],fill=(60,60,60)); d.rectangle([x,y+h-14,x+w,y+h],fill=(20,20,30))
    elif k=="gate":
        d.rectangle([x,y+h-30,x+w,y+h],fill=(120,30,30)); d.rectangle([x+w*0.08,y+22,x+w*0.20,y+h-30],fill=(150,40,40)); d.rectangle([x+w*0.80,y+22,x+w*0.92,y+h-30],fill=(150,40,40)); d.rectangle([x+w*0.20,y+30,x+w*0.80,y+h-30],fill=(200,170,90)); d.rectangle([x+w*0.38,y+52,x+w*0.62,y+h-30],fill=(90,20,20)); d.rectangle([x+w*0.30,y+18,x+w*0.70,y+30],fill=(178,34,34)); d.rectangle([x+w*0.46,y+34,x+w*0.54,y+48],fill=(255,255,255))
    elif k=="court":
        d.rectangle([x,y+h-22,x+w,y+h],fill=(70,70,80)); d.polygon([(x+w*0.10,y+38),(x+w*0.50,y+8),(x+w*0.90,y+38)],fill=(40,52,80)); d.rectangle([x+w*0.14,y+38,x+w*0.86,y+h-22],fill=(220,220,210)); d.rectangle([x+w*0.42,y+46,x+w*0.58,y+h-22],fill=(60,60,70))
        for i in range(4): d.rectangle([x+w*0.18+i*w*0.17,y+46,x+w*0.24+i*w*0.17,y+h-22],fill=(150,150,140))
        d.rectangle([x+w*0.68,y+52,x+w*0.92,y+66],fill=(178,34,34)); d.text((x+w*0.70,y+54),"10/12",font=fb(11),fill=(255,255,255))
    elif k=="drones":
        d.rectangle([x,y,x+w,y+22],fill=(20,28,48)); d.rectangle([x,y+h-16,x+w,y+h],fill=(60,50,40))
        for i in range(3): d.ellipse([x+w*0.15+i*w*0.28,y+34,x+w*0.25+i*w*0.28,y+44],fill=(255,180,60))
        d.polygon([(x+w*0.10,y+h-16),(x+w*0.30,y+52),(x+w*0.50,y+h-16)],fill=(90,80,70)); d.polygon([(x+w*0.55,y+h-16),(x+w*0.75,y+58),(x+w*0.95,y+h-16)],fill=(80,70,60))
    elif k=="trophy":
        d.rectangle([x,y,x+w,y+h],fill=(20,80,50)); d.ellipse([x+w*0.38,y+16,x+w*0.62,y+44],fill=(255,210,60)); d.rectangle([x+w*0.46,y+42,x+w*0.54,y+62],fill=(255,210,60)); d.rectangle([x+w*0.36,y+62,x+w*0.64,y+70],fill=(200,160,40)); d.rectangle([x+w*0.06,y+10,x+w*0.20,y+18],fill=(0,120,60)); d.rectangle([x+w*0.80,y+10,x+w*0.94,y+18],fill=(200,40,40))
    elif k=="ship":
        d.rectangle([x,y,x+w,y+h],fill=(180,210,230)); d.rectangle([x,y+h-26,x+w,y+h],fill=(30,70,110)); d.rectangle([x+w*0.12,y+34,x+w*0.88,y+h-26],fill=(178,60,40)); d.rectangle([x+w*0.12,y+34,x+w*0.88,y+44],fill=(40,60,90))
        for i in range(5): d.rectangle([x+w*0.16+i*w*0.14,y+46,x+w*0.26+i*w*0.14,y+56],fill=(255,220,120))
        d.rectangle([x+w*0.70,y+18,x+w*0.76,y+34],fill=(60,60,60)); d.ellipse([x+w*0.80,y+12,x+w*0.94,y+26],fill=(255,120,40))
    elif k=="chart":
        d.rectangle([x,y,x+w,y+h],fill=(245,245,235)); d.line([(x+8,y+h-14),(x+w-8,y+14)],fill=(178,34,34),width=3); d.line([(x+8,y+h-14),(x+w-8,y+h-14)],fill=(0,0,0),width=2); d.line([(x+8,y+14),(x+8,y+h-14)],fill=(0,0,0),width=2)
        for i in range(4): d.rectangle([x+16+i*22,y+h-20-i*9,x+32+i*22,y+h-14],fill=(30,90,50))
        d.text((x+10,y+6),"50,018",font=fb(13),fill=(178,34,34))
    elif k=="server":
        d.rectangle([x,y,x+w,y+h],fill=(30,30,40)); d.rectangle([x+w*0.12,y+12,x+w*0.88,y+h-12],fill=(60,60,75)); d.rectangle([x+w*0.16,y+18,x+w*0.84,y+30],fill=(178,34,34)); d.text((x+w*0.20,y+19),"CODE RED",font=fb(10),fill=(255,255,255))
        for i in range(3): d.rectangle([x+w*0.16,y+36+i*12,x+w*0.84,y+44+i*12],fill=(90,200,120))
    elif k=="heli":
        d.rectangle([x,y,x+w,y+h],fill=(200,220,235)); d.polygon([(x,y+h),(x+w*0.35,y+34),(x+w,y+h)],fill=(120,130,110)); d.ellipse([x+w*0.32,y+26,x+w*0.62,y+46],fill=(60,80,60)); d.rectangle([x+w*0.60,y+32,x+w*0.94,y+38],fill=(60,80,60)); d.line([(x+w*0.20,y+24),(x+w*0.80,y+24)],fill=(40,40,40),width=3)
    elif k=="market":
        d.rectangle([x,y,x+w,y+h],fill=(240,230,200)); d.rectangle([x+w*0.10,y+26,x+w*0.90,y+h-10],fill=(200,80,60)); d.polygon([(x+w*0.05,y+28),(x+w*0.50,y+8),(x+w*0.95,y+28)],fill=(150,40,40)); d.rectangle([x+w*0.42,y+44,x+w*0.58,y+h-10],fill=(90,30,30))
    elif k=="desert":
        d.rectangle([x,y,x+w,y+22],fill=(255,220,140)); d.rectangle([x,y+22,x+w,y+h],fill=(230,190,120)); d.polygon([(x,y+h),(x+w*0.30,y+40),(x+w*0.60,y+h)],fill=(210,170,90)); d.ellipse([x+w*0.70,y+8,x+w*0.86,y+24],fill=(255,200,60))
    elif k=="strike":
        d.rectangle([x,y,x+w,y+h],fill=(210,200,180)); d.rectangle([x+w*0.10,y+44,x+w*0.55,y+56],fill=(60,60,70)); d.ellipse([x+w*0.12,y+34,x+w*0.26,y+48],fill=(40,40,50)); d.ellipse([x+w*0.62,y+16,x+w*0.84,y+38],fill=(255,140,40)); d.ellipse([x+w*0.68,y+22,x+w*0.78,y+32],fill=(255,210,80))
    else:
        d.rectangle([x,y,x+w,y+h],fill=(20,40,80)); d.ellipse([x+w*0.36,y+12,x+w*0.64,y+40],fill=(200,220,255)); d.polygon([(x+w*0.42,y+40),(x+w*0.50,y+8),(x+w*0.58,y+40)],fill=(220,220,220)); d.rectangle([x+w*0.30,y+52,x+w*0.70,y+60],fill=(255,210,90)); d.rectangle([x+w*0.44,y+60,x+w*0.56,y+70],fill=(200,160,40))
    _IM.paste(_tmp.resize((int(_ow),int(_oh))),(int(_ox),int(_oy)))

RED=(178,34,34); NAVY=(20,40,80); CREAM=(250,244,230); INK=(15,15,15); GREY=(90,90,90); GREEN=(34,120,60); BLUE=(30,80,160); ORANGE=(200,100,20)
HERO=[("1  RIYADH","MIDDLE EAST","CONFIRMED","tower","Houthi drone hits Riyadh's tallest tower again, 11 hurt","Houthi drone hits the PIF tower — the tallest in Riyadh — a second strike in a week. 11 hurt: 2 Saudi, 2 India, 3 Nepal, 4 Egypt. (Saudi officials · 14:27 UTC)"),("2  SHANGHAI","ASIA","OFFICIAL","gate","China probes Shanghai party chief Chen Jining","Chen Jining, 62, is probed for \u201cserious violations\u201d — the 4th Politburo member to fall in a probe this year, the biggest elite shock of 2026. (CCDI)"),("3  NEW YORK","US / TECH","CONFIRMED","court","Huawei guilty on 10 of 12 counts","A US federal jury finds Huawei guilty on 10 of 12 counts — trade-secret theft and bank fraud. Cleared of racketeering. Sentencing Sep 2027; Huawei appeals. (US court · 20:41 UTC)")]
CARDS=[("4  ZAPORIZHZHIA","EUROPE / WAR","REPORTED","drones","Russian attacks kill 9 across Ukraine in a day","9 dead, 81 hurt; 96 drones launched, 73 shot down. (Ukraine · 11:37 UTC)"),("5  CAS","AFRICA / SPORT","OFFICIAL","trophy","CAS hands Senegal back the AFCON title","Morocco forfeit 3-0, so Senegal win 1-0 and take the Africa Cup back. (CAS)"),("6  HORMUZ","MIDDLE EAST","REPORTED","ship","IRGC attacks container ship in Hormuz","Ship attacked 18:58 UTC; navigation off, no-go zone north of Khasab. (UKMTO)"),("7  NEW YORK","WORLD / MARKETS","CONFIRMED","chart","Dow closes above 50,000 for the first time","Dow 50,018. Nasdaq -1.5%. Taiex +8.99% to record 40,122. (Market close)"),("8  REDMOND","WORLD / TECH","REPORTED","server","Microsoft declares \u2018Code Red\u2019 after historic outage","24-hour outage 12-13 Nov; Microsoft targets 1-hour recovery. (Reuters)"),("9  ESKISEHIR","EUROPE","REPORTED","heli","Turkish military helicopter crash kills 5","AS-532 helicopter crashes in Eskisehir; 5 dead. (Turkey · 19:52 UTC)"),("10  CARTAGENA","AMERICAS","REPORTED","market","Supermarket hostages: 25 held in Cartagena","25 hostages held; 5 elderly women freed; landings halted ~45 min. (Colombia)"),("11  ADEN","MIDDLE EAST","REPORTED","desert","Houthis advance within 60 km of Aden","Houthi forces advance to within 60 km of Aden, Yemen. (Wires · 16:51 UTC)"),("12  LAHJ","MIDDLE EAST","REPORTED","strike","Saudi strikes kill 25, wound 6 in Yemen","Bus and truck hit in Wadi Maabaq: 25 dead or missing, 6 wounded. (Yemen)"),("13  JIUQUAN","WORLD / SPACE","OFFICIAL","rocket","China names first foreign astronaut for Tiangong","Crew: Tang Hongbo, Wu Yi, Zeeshan Ali (Pakistan), first on Tiangong. (CMSA)")]
UTC=[("02:15","NATO vows space defence"),("08:16","Hanoi hot-pot blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
NUMS=[("11","hurt in Riyadh drone hit"),("9","dead in Ukraine in a day"),("50,018","Dow, first close over 50,000"),("+8.99%","Taiex, record 40,122"),("25","dead or missing in Yemen"),("26","Cikande factory-fire toll"),("10/12","Huawei guilty counts"),("5,258","record heat deaths, England")]
ALSO=[(14,"Ankara","Haftar visits Turkey for the first time"),(15,"London","UK sanctions Houthis + 4 officials"),(16,"Villavicencio","Car bomb injures 23"),(17,"Gaza","Israel kills Hamas security chief, +6"),(18,"Baghdad","Iraq orders federal control of Kurdish oilfields"),(19,"Gaza","Meningitis alert: 272 cases in Oct, 15 dead in 2026"),(20,"DR Congo","Missing Cessna 208; rebels claim shootdown, 4 aboard"),(21,"Hanoi","Hot-pot blast kills \u22656, \u226510 hurt"),(22,"Gulf of Finland","Ukraine hits Russian ship Sparta II, 16 evacuated"),(23,"Kuala Lumpur","Malaysia to return migrants: 1,500 by sea, 5,303 by air"),(24,"Ulleungdo","S. Korea shelter order as Russian jets enter ADIZ"),(25,"Dhaka","Hasina plans return 16 Dec"),(26,"The Hague","14 nations endorse ICJ Myanmar ruling, 9-6"),(27,"Jakarta","Indonesia nominates 2 VP candidates"),(28,"Beijing","China sentences official Ma to death for spying, 35 secrets"),(29,"Brussels","NATO vows defence against space threat"),(30,"Mexico City","El Chapo Isidro: US drone aided weekend capture"),(31,"San Salvador","Bukele names 3 Salvadoran soldiers killed in Haiti"),(32,"Ottawa","Pentagon rebukes Canada: only 41.9% of air fleet ready"),(33,"Washington","US adds Megaspeed to trade blacklist"),(34,"Kyiv","Zelensky urges Ukraine / Russia / US / Europe talks soon"),(35,"Ras Al Khaimah","UAE bus-truck crash kills 13; bus carried 41"),(36,"London","England record 5,258 heat deaths, summer 2026"),(37,"Kourou","Ariane 6 lofts 36 Amazon satellites"),(38,"Cikande","Factory-fire toll rises to 26")]
PINS=[(1,24.7,46.7),(2,31.2,121.5),(3,40.7,-74.0),(4,47.8,35.2),(5,14.7,-17.4),(6,26.5,56.2),(7,40.7,-74.0),(8,47.7,-122.1),(9,39.8,30.5),(10,10.4,-75.5),(11,12.8,45.0),(12,13.0,44.9),(13,39.7,98.5)]
CONT=[ [(-168,66),(-140,70),(-120,72),(-95,80),(-80,73),(-60,60),(-55,47),(-70,42),(-75,35),(-80,25),(-90,21),(-97,16),(-105,20),(-115,30),(-125,40),(-125,49),(-145,60),(-165,60)], [(-80,10),(-60,5),(-50,0),(-35,-8),(-40,-20),(-50,-30),(-65,-40),(-70,-52),(-73,-40),(-70,-20),(-80,-5)], [(-10,36),(-9,43),(0,48),(-5,50),(5,58),(10,58),(20,60),(25,70),(35,68),(40,60),(30,55),(25,45),(20,40),(10,38),(0,36)], [(-17,15),(-10,30),(10,37),(20,32),(32,31),(43,12),(51,11),(45,0),(40,-10),(35,-20),(30,-30),(20,-35),(15,-25),(12,-5),(9,4),(-8,5)], [(40,60),(60,70),(100,75),(140,72),(170,66),(180,65),(160,60),(140,45),(130,35),(120,25),(108,10),(100,5),(95,15),(85,20),(75,8),(65,25),(55,25),(45,30),(40,35)], [(113,-22),(130,-12),(142,-11),(150,-22),(150,-37),(140,-38),(130,-32),(115,-35)] ]
def main():
    W=1024; H=1024; M=16; CW=W-2*M
    im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im); globals()["_IM"]=im
    d.rectangle([0,0,W,5],fill=RED)
    d.text((M,10),"THE WORLD ON ONE DAY",font=fb(10),fill=RED); d.text((M+560,10),"38 STORIES  \u00b7  7 REGIONS  \u00b7  14 FIELDS  \u00b7  ALL FROM TUESDAY 24 NOVEMBER 2026",font=fb(9),fill=NAVY)
    d.text((M,26),"Tuesday 24 November 2026",font=fser(30),fill=INK); d.text((M,60),"Riyadh tower hit again  \u00b7  Shanghai party chief probed  \u00b7  Huawei guilty 10 of 12",font=fs(12),fill=RED)
    d.line([(M,80),(W-M,80)],fill=INK,width=2)
    rb=[("Europe",7,(40,80,160)),("Middle East",8,(178,34,34)),("Asia",9,(200,120,20)),("Africa",5,(34,120,60)),("Americas",5,(90,60,140)),("Oceania",0,(90,90,90)),("World / Space",4,(20,40,80))]
    x=M; y=86
    for nm,n,c in rb:
        w=44 if n==0 else int(930*n/38); d.rectangle([x,y,x+w,y+16],fill=c); d.text((x+4,y+3),f"{nm} {n}",font=fb(8),fill=(255,255,255)); x+=w+3
    y=108; d.text((M,y),"THE DAY IN UTC",font=fb(10),fill=RED)
    for i,(t,ev) in enumerate(UTC):
        cx=M+i*142; d.text((cx,y+14),t,font=fb(11),fill=NAVY); lines(d,cx,y+28,ev,fs(8),132,2,INK,10)
    d.line([(M,158),(W-M,158)],fill=(180,180,180),width=1)
    y=164; d.text((M,y),"THE DAY IN NUMBERS",font=fb(10),fill=RED)
    for i,(v,lab) in enumerate(NUMS):
        cx=M+i*124; d.text((cx,y+14),v,font=fb(17),fill=RED); lines(d,cx,y+34,lab,fs(8),116,2,INK,10)
    d.line([(M,222),(W-M,222)],fill=(180,180,180),width=1)
    y=230; hw=322; gap=13
    for i,(loc,field,ch,k,head,deck) in enumerate(HERO):
        x=M+i*(hw+gap); scene(d,x,y,hw,92,k); d.rectangle([x,y+92,x+hw,y+186],fill=(255,255,255),outline=(200,200,200))
        d.text((x+6,y+96),loc,font=fb(9),fill=NAVY); cc=GREEN if ch=="CONFIRMED" else BLUE; chip(d,x+hw-72,y+96,ch,cc)
        lines(d,x+6,y+112,head,fb(12),hw-12,2,INK,14); lines(d,x+6,y+142,deck,fs(9),hw-12,3,INK,11)
    y=424; cw2=190; g2=10
    for r in range(2):
        for c in range(5):
            i=r*5+c; loc,field,ch,k,head,deck=CARDS[i]; x=M+c*(cw2+g2); yy=y+r*86
            scene(d,x,yy,cw2,26,k); d.rectangle([x,yy+26,x+cw2,yy+86],fill=(255,255,255),outline=(200,200,200))
            d.text((x+5,yy+29),loc,font=fb(8),fill=NAVY); cc=GREEN if ch=="CONFIRMED" else BLUE if ch=="OFFICIAL" else GREY; chip(d,x+cw2-62,yy+29,ch,cc)
            lines(d,x+5,yy+43,head,fb(9),cw2-10,2,INK,11); lines(d,x+5,yy+64,deck,fs(8),cw2-10,2,INK,10)
    y=602; mx,my,mw,mh=M,y,640,116; d.rectangle([mx,my,mx+mw,my+mh],fill=(185,215,235),outline=(120,120,120))
    def proj(lon,lat): return (mx+(lon+180)/360*mw, my+(75-lat)/132*mh)
    for poly in CONT:
        pts=[proj(lo,la) for lo,la in poly]; d.polygon(pts,fill=(120,170,110),outline=(60,100,60))
    off={7:(14,-12),12:(10,10),3:(0,0)}
    for n,lat,lon in PINS:
        px,py=proj(lon,lat); dx,dy=off.get(n,(0,0)); px+=dx; py+=dy; d.ellipse([px-8,py-8,px+8,py+8],fill=RED,outline=(255,255,255)); d.text((px-3,py-6),str(n),font=fb(8),fill=(255,255,255))
    lx=mx+mw+12; d.text((lx,my),"MAP  \u00b7  STORIES 1-13",font=fb(10),fill=NAVY)
    lines(d,lx,my+16,"Pins are numbered by story. 1 Riyadh  \u00b7  2 Shanghai  \u00b7  3 New York  \u00b7  4 Zaporizhzhia  \u00b7  5 Dakar  \u00b7  6 Hormuz  \u00b7  7 New York  \u00b7  8 Redmond  \u00b7  9 Eskisehir  \u00b7  10 Cartagena  \u00b7  11 Aden  \u00b7  12 Lahj  \u00b7  13 Jiuquan.",fs(9),W-M-lx,8,INK,12)
    d.text((lx,my+92),"Red pin = story number. Colours in the region bar above match each story's region.",font=fs(8),fill=GREY)
    y=726; d.text((M,y),"ALSO ON TUESDAY  \u2014  25 MORE STORIES",font=fb(11),fill=NAVY); d.line([(M,y+16),(W-M,y+16)],fill=INK,width=1)
    colw=326
    for idx,(n,city,head) in enumerate(ALSO):
        col=idx//9; row=idx%9; x=M+col*(colw+6); yy=y+22+row*15; d.text((x,yy),f"{n}.",font=fb(8),fill=RED); lines(d,x+18,yy,f"{city}: {head}",fs(8),colw-18,1,INK,10)
    y=726+22+9*15+6; d.rectangle([M,y,W-M,y+118],fill=(255,240,240),outline=RED)
    d.text((M+8,y+6),"DATE CHECK",font=fb(11),fill=RED)
    lines(d,M+8,y+22,"Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.",fb(9),CW-16,1,INK,12)
    lines(d,M+8,y+38,"LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) \u00b7 Huang returns as Nvidia CEO (23 Nov) \u00b7 EU sanctions package 22 (23 Nov) \u00b7 COP31 ends with no deal (22 Nov) \u00b7 corvette Merkury sunk (22 Nov) \u00b7 El Chapo Isidro captured (20 Nov) \u00b7 Cikande factory fire started (21 Nov) \u00b7 Trump hush-money appeal ruling (23 Nov) \u00b7 ATP Final (22 Nov) \u00b7 F1 Las Vegas GP (21 Nov).",fs(9),CW-16,2,INK,11)
    lines(d,M+8,y+64,"NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) \u00b7 MPR vote for Vice President (11 Dec) \u00b7 Huawei sentencing (Sep 2027) \u00b7 Hasina returns to Bangladesh (16 Dec).",fs(9),CW-16,2,INK,11)
    lines(d,M+8,y+88,"Note: the 24 Nov Hormuz story is the IRGC container-ship attack (18:58 UTC), not the mine claims; the 24 Nov El Chapo story is the US drone role and Mexico's decision to try him; the 24 Nov Cikande story is the toll rising to 26.",fs(8),CW-16,2,GREY,10)
    y=y+126; d.text((M,y),"Sources: dailysummaryof.com \u00b7 Reuters \u00b7 AP \u00b7 WSOC \u00b7 CCDI \u00b7 CAS \u00b7 UKMTO \u00b7 CMSA \u00b7 UKHSA",font=fs(8),fill=GREY)
    d.text((M,y+12),"CONFIRMED = 2+ outlets  \u00b7  OFFICIAL = on record  \u00b7  REPORTED = one outlet  \u00b7  CLAIM = one party's claim  \u00b7  ONGOING = still running",font=fs(8),fill=GREY)
    d.text((M,y+24),"Scenes are drawn illustrations, not photographs. All figures as reported on 24 November 2026.",font=fs(8),fill=GREY)
    out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True); im.save(out)
if __name__=="__main__": main()
