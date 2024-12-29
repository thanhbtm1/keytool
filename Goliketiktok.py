import os,time
try:
  import requests
except:
  os.system("pip install requests")
  import requests
from time import sleep
banner = """
          \033[1;35m████████╗░█████╗░████████╗
          \033[1;34m╚══██╔══╝██╔══██╗ ╚══██╔══╝
          \033[1;35m   ██║   ██║  ╚═╝    ██║
          \033[1;36m   ██║   ██║  ██     ██║
          \033[1;32m   ██║   ╚█████╔╝    ██║
          \033[1;34m   ╚═╝    ╚════╝     ╚═╝

                      \033[1;36m████████╗  ████╗  █████╗ ██╗
                      \033[1;35m╚══██╔══╝██╔══██╗██╔══██╗██║
                      \033[1;33m   ██║   ██║  ██║██║  ██║██║
                      \033[1;32m   ██║   ██║  ██║██║  ██║██║
                      \033[1;34m   ██║   ╚█████╔╝╚█████╔╝███████╗
                      \033[1;36m   ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[1;35m═════════════════════════════════════════════════════════════
\033[1;36m@COPYRIGHT : Thành Chần 🤡
\033[1;34mZalo : 0335021778 💍
\033[1;35mNhóm Zalo : https://zalo.me/g/drghio579
\033[1;35m═════════════════════════════════════════════════════════════"""
os.system("clear")
print(banner)   
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;36mNhập Authorization : ")
  token = input("\033[1;36mNhập T : ")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;33mBạn có muốn đổi acc golike???(enter để bỏ qua,nhập Authorization acc khác để đổi) : ")
  if select != "":
    author = select
    token = input("\033[1;36mNhập T : ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  while True:
    try:
      if(chontktiktok["status"]!=200):
        print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
        quit()
      print("\033[1;33mDanh sách acc tóp tóp : ")  
      print("\033[1;33m═════════════════════════════════════════════════════════════")
      for i in range(len(chontktiktok["data"])):
        print(f'\033[1;36m[●] ID : {chontktiktok["data"][i]["unique_username"]}')
      print("\033[1;33m═════════════════════════════════════════════════════════════")   
      break
    except:
      print(f"\033[1;36m{chontktiktok}")
      sleep(10)
dsacc() 
# while True:
#   try:
#     luachon = int(input("\033[1;35mChọn acc để làm nhiệm vụ : "))
#     while luachon > len((chontktiktok)["data"]):
#       luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách,Hãy Nhập Lại : "))
#     account_id = chontktiktok["data"][luachon - 1]["id"]
#     account_name = chontktiktok["data"][luachon - 1]["unique_username"]
#     break  
#   except:
#     print("\033[1;35mSai định dạng!!!")
d = 0  
while True:   
  idacc = str(input("\033[1;36mNhập id acc tiktok làm việc: "))  
  for i in range(len(chontktiktok["data"])):
    if chontktiktok["data"][i]["unique_username"] == idacc:
      d = 1
      account_id = chontktiktok["data"][i]["id"]
      break 
  if d == 0:
    print("\033[1;31mAcc này chưa được thêm vào golike or id sai")
    continue
  break    
while True:
  try:
    delay = int(input("\033[1;36mNhập thời gian làm job : "))
    break
  except:
    print("\033[1;31mSai định dạng!!!")
while True:
  try:
    lannhan = input("\033[1;36mBạn có muốn nhận tiền lần 2 nếu lần 1 fail không (y/n) ")
    if lannhan != "y" and lannhan != "n":
      print("\033[1;31mNhập sai hãy nhập lại!!!")
      continue
    break
  except:
    pass
  
while True:
  try: 
    doiacc = int(input("\033[1;36mSau bao nhiêu job fail thì yêu cầu đổi acc tiktok (không muốn thì cứ nhập 1 số siêu to khổng lồ) : "))
    break
  except:
    print("\033[1;31mNhập vào 1 số!!!")    
os.system("clear")    
dem = 0
tong = 0
checkdoiacc = 0
checkdoiacc1 = 0
dsaccloi = []
accloi = ""
os.system("clear")
print(banner)
lam = ["follow"]
i = """
if(chedo == 1):
  lam = ["follow"]
elif(chedo == 2):
  lam = ["like"]
elif(chedo == 12):
  lam = ["follow","like"]"""
while True:
  if checkdoiacc == doiacc:
    dsacc()
    idacc = str(input(f"\033[1;31mJob fail đã đạt giới hạn nên nhập id acc khác để đổi: "))
    d = 0 
    for i in range(len(chontktiktok["data"])):
      if(chontktiktok["data"][i]["unique_username"]) == idacc:
        d = 1;
        account_id = chontktiktok["data"][i]["id"]
        break
    if d == 0:
      print("\033[1;31mAcc này chưa được thêm vào golike or id sai")
      continue
    checkdoiacc = 0
  print("                                     ",end = "\r") 
  print("\033[1;33mĐang tìm chốp:))",end = "\r")        
  while True:
    try:  
      nhanjob = nhannv(account_id)
      break
    except:
      # nhanjob = nhannv(account_id)
      # print(nhanjob)
      pass
  if("status" in nhanjob and nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    loai = nhanjob["data"]["type"]
    if(nhanjob["data"]["type"] not in lam):
      try:
        baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
        print("                                             ",end = "\r")
        print(f"\033[1;36mĐang bỏ qua job {loai}",end = "\r")
        sleep(1)
        continue
      except:
        pass
    if loai == "follow": 
      loainv = "follow"
    elif loai == "like":
      loainv = " like "    
    os.system(f"termux-open-url {link}")
    for i in range(delay,-1,-1):
      print('                                             ',end = '\r')
      for j in ['','.','..','...']:
        print("\033[1;36m"+f"Bạn Còn {i} Giây Để Làm Nhiệm Vụ{j}",end ='\r')
        time.sleep(1/4)
    print("                                                ",end = "\r")    
    print("\033[1;35mĐang nhận tiền lần 1:>",end = "\r")
    while True:    
      try:    
        nhantien = hoanthanh(ads_id,account_id)
        break
      except:
        pass
    if(lannhan == "y"):
      checklan = 1
    else:
      checklan = 2
    ok = 0
    while checklan <= 2:  
      if("status" in nhantien and nhantien["status"] == 200):
        ok = 1
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if(hour < 10):
          h = "0"+str(hour)
        if(minute < 10):
          m = "0"+str(minute)
        if(second < 10):
          s = "0"+str(second)
        print("                                                    ",end = "\r")
        chuoi = f"\033[1;32m✯ {dem} ✈ \033[1;31m{idacc} ●\033[1;34m {loainv} ●\033[1;35m {h}:{m}:{s} ●\033[1;36m +{tien} ✈ \033[1;32mTổng: {tong} VNĐ" 
        print(chuoi)    
        checkdoiacc = 0  
        break
      else:
        checklan+=1
        if checklan == 3:
          break
        print("                                 ",end = "\r")
        print("\033[1;35mĐang nhận tiền lần 2:>",end = "\r")
        nhantien = hoanthanh(ads_id,account_id)
    if ok != 1:
      while True:
        try:  
          baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
          print("                                              ",end = "\r")
          print("\033[1;36mBỏ Qua Job!!!",end = "\r")
          sleep(1)
          checkdoiacc+=1
          break
        except:
          qua = 0
          pass
  else:
    sleep(10)
        