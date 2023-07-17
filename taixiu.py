import random
import os
import sys
import time
from colorama import Fore, Style
a = random.randint(1,10000000000000)
b = random.randint(1,10000000000000)
os.system("clear")
print(Fore.YELLOW + '''1.Tài\n2.Xỉu''' + Style.RESET_ALL)
sd = input(Fore.YELLOW + "Lựa chọn:" + Style.RESET_ALL)
if sd =='1':
	print("Tài:",a)
elif sd=='2':
	print("Xỉu:",b)
if a>b:
	print(Fore.YELLOW + "Tài thắng Xỉu Thua" + Style.RESET_ALL)
if b>a:
	print(Fore.YELLOW + "Xỉu thắng Thằng nào chọn tài nhục như con chó!" + Style.RESET_ALL)