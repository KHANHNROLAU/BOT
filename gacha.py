import random
import os
import sys
from colorama import Fore, Style
os.system("clear")
a = random.randint(1,100000000000000000000)
b = random.randint(1,199)
c = random.randint(1,199)
d = random.randint(1,99)
m = random.randint(1,199)
print(Fore.YELLOW + "1.Random số\n2.Random ip\n3.Thử Vận may" + Style.RESET_ALL)
sd = input(Fore.YELLOW + "Lựa chọn:" + Style.RESET_ALL)
if sd=='1':
	print("Số bạn là:",a)
elif sd =='2':
	print("Tự copy r thêm dấu chấm vào nhé ví dụ là 195.121.54.199")
	print(b)
	print(c)
	print(d)
	print(m)
elif sd=='3':
	print("Admin sẽ update sau")