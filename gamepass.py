import os
import sys
from colorama import Fore, Style
os.system("clear")
print(Fore.YELLOW + "1.Tài xỉu\n2.Gacha\3.Thoát" + Style.RESET_ALL)
sd = input(Fore.YELLOW + "Lựa chọn:" + Style.RESET_ALL)
if sd=='1':
	os.system("python taixiu.py")
elif sd=='2':
	os.system("python gacha.py")