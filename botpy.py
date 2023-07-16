import os
import sys
import time
import random
from colorama import Fore, Style
am = random.randint(1,99999999999999)
a = '''  ____            _   
 | __ )    ___   | |_ 
 |  _ \   / _ \  | __|
 | |_) | | (_) | | |_ 
 |____/   \___/   \__|'''
os.system("clear")
print(Fore.CYAN + a + Style.RESET_ALL)
rt = input(Fore.YELLOW + "Chat:" + Style.RESET_ALL)
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
	print(Fore.CYAN + "Basic:Free" + Style.RESET_ALL)
elif rt == 'zalo':
	print(Fore.YELLOW + "https://zalo.me/g/ctukrh452" + Style.RESET_ALL)
elif rt =='help':
	print(Fore.CYAN + "Command:info\nrandom\nkick\nsex\nzalo\ntype\nvip1\nshow\nbot\nslot\nslot2" + Style.RESET_ALL)
elif rt =='show':
	print(Fore.YELLOW + "Vps:admin@v9376\nPassword:tcp472towifn" + Style.RESET_ALL)
elif rt=='bot':
	print(Fore.CYAN + "Bot day anh co dieu gi mun hoi?"+ Style.RESET_ALL)
elif rt=='slot':
	print(Fore.YELLOW + "Link nhom ghi vo day" + Style.RESET_ALL)
elif rt=='slot2':
	print(Fore.YELLOW + "Link nhom ghi vo day" + Style.RESET_ALL)