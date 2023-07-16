import os
import sys
import time
import random
from colorama import Fore, Style
aml = random.randint(1,1000)
alm = random.randint(1,1000)
os.system("clear")
user = input("Username:")
if user == 'login':
	print("dung rui")
else:
	quit()
os.system("clear")
ams = '___________________________________________'
a = '''___   _                    _       _ 
 |_ _| | |_    __ _    ___  | |__   (_)
  | |  | __|  / _` |  / __| | '_ \  | |
  | |  | |_  | (_| | | (__  | | | | | |
 |___|  \__|  \__,_|  \___| |_| |_| |_|'''
print(Fore.RED + a + Style.RESET_ALL)
print(Fore.YELLOW + ams + Style.RESET_ALL)
rt = input("Lua chon:")
if rt =='tiktok':
	os.system("python tiktok.py")
if rt == 'info':
	print(Fore.MAGENTA + "HuuMinh:Membory:1\nBot:HuuMinh\nOnline:1" + Style.RESET_ALL)
elif rt == 'random':
	print(am)
elif rt =='stop':
	print("Stop succes!")
	quit()
elif rt =='vip1':
	os.system("clear")
	os.system("python vip1.py")
elif rt =='sex':
	print(Fore.YELLOW + "Link 1:https://vlxyz.tv/page/22/\nLink 2:https://sexdotz.com/phim-sex-hay/page/2/\nLink 3:https://web.sexnhanh.co/\nLink 4:https://hentaikhongche.net/\nLink 5:https://hentaimoi.com/" + Style.RESET_ALL)
elif rt =='kick':
	print(Fore.RED + "Chuc nang kick chi hoat dong khi co member!"+ Style.RESET_ALL)
elif rt =='type':
	print(Fore.CYAN + "Basic:Buy" + Style.RESET_ALL)
elif rt == 'zalo':
	print(Fore.YELLOW + "https://zalo.me/g/ctukrh452" + Style.RESET_ALL)
elif rt =='help':
	print(Fore.CYAN + "Command:info\nrandom\nkick\nsex\nzalo\ntype\nvip1\nshow\nbot\nslot\nslot2\ntiktok\ninfo1\nmembery\nin4\nspam\nexit\nexit\ngame\nrank" + Style.RESET_ALL)
elif rt =='show':
	print(Fore.YELLOW + "Vps:admin@v9376\nPassword:tcp472towifn" + Style.RESET_ALL)
elif rt=='bot':
	print(Fore.CYAN + "Bot day anh co dieu gi mun hoi?"+ Style.RESET_ALL)
elif rt=='slot':
	print(Fore.YELLOW + "Link nhom ghi vo day" + Style.RESET)
elif rt=='slot2':
	print(Fore.YELLOW + "Link nhom ghi vo day" + Style.RESET_ALL)
elif rt=='info1':
	print(Fore.YELLOW + "Fb:Nguyen Huu Minh" + Style.RESET_ALL)
	print(Fore.CYAN + "Id:Vi thong tin ca nhan nen khong tiet lo!" + Style.RESET_ALL)
	print(Fore.BLUE + "Link:Khong tiet lo vi thong tin ca nhan!" + Style.RESET_ALL)
elif rt=='membery':
	print(Fore.CYAN + "Box:Test bot python" + Style.RESET_ALL)
	print(Fore.YELLOW + "Admin:Nguyen Huu Minh" + Style.RESET_ALL)
	print(Fore.RED + "language:Python" + Style.RESET_ALL)
elif rt =='in4':
	print(Fore.YELLOW + "Link ghi vo day" + Style.RESET_ALL)
elif rt=='spam':
	print(Fore.CYAN + "Spam gi ghi vo day"*10000 + Style.RESET_ALL)
elif rt=='exit':
	quit()
elif rt=='game':
	os.system("python game.py")
elif rt=='rank':
	print(Fore.YELLOW + "Rank:Vip1" + Style.RESET_ALL)