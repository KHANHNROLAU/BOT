import time
import sys
import os
from colorama import Fore, Style
os.system("clear")
giay=time.time()
sex=time.ctime(giay)
print(Fore.YELLOW + "Bây giờ là:",sex + Style.RESET_ALL)
print(Fore.CYAN + "1 Chơi" + Style.RESET_ALL)
print(Fore.RED + "2.Thoát" + Style.RESET_ALL)
sd = input(Fore.YELLOW + "Lựa chọn:" + Style.RESET_ALL)
if sd=='1':
	os.system("python gamepass.py")
elif sd =='2':
	os.system("clear")
	quit()