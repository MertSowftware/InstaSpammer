import os
os.system("clear")
os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install pathlib")
os.system("pip install bs4")
os.system("clear")
from colorama import Fore
print(Fore.GREEN + "İzin Vere Tıklayınız Eğer İzin Ver Tuşu Yoksa Y Tuşuna Basıp Enterleyiniz." + Fore.WHITE)
os.system("termux-setup-storage")
os.system("python InstaSpammer.py")
