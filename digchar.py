import os
import time
import requests
import platform
from colorama import Fore, Style

print(Fore.CYAN + "")

os.system("pip3 install requests")

os.system("figlet isletim")
system_info = {}

system_info['İşletim Sistemi'] = platform.system()

system_info['Sürüm'] = platform.release()

system_info['Mimarisi'] = platform.machine()

for category, info in system_info.items():

    print(category)

    print('=' * 30)

    print(info)

    print()

time.sleep(3)
print("")
time.sleep(2)
print("————————⟩%5")
time.sleep(1)
print("")
print("————————⟩%10")
time.sleep(1)
print("")
print("————————⟩%20")
time.sleep(1)
print("")
print("————————⟩%30")
time.sleep(1)
print("")
print("————————⟩%40")
time.sleep(1)
print("")
print("————————⟩%50")
time.sleep(1)
print("")
print("————————⟩%80")
time.sleep(1)
print("")
print("————————⟩%95")
time.sleep(1)
print("")
print("————————⟩%100")
time.sleep(1)

print(Fore.GREEN +"""
@@@@@@@   @@@   @@@@@@@@   @@@@@@@  @@@  @@@   @@@@@@   @@@@@@@   
@@@@@@@@  @@@  @@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!  !@@        !@@       @@!  @@@  @@!  @@@  @@!  @@@  
!@!  @!@  !@!  !@!        !@!       !@!  @!@  !@!  @!@  !@!  @!@  
@!@  !@!  !!@  !@! @!@!@  !@!       @!@!@!@!  @!@!@!@!  @!@!!@!   
!@!  !!!  !!!  !!! !!@!!  !!!       !!!@!!!!  !!!@!!!!  !!@!@!    
!!:  !!!  !!:  :!!   !!:  :!!       !!:  !!!  !!:  !!!  !!: :!!   
:!:  !:!  :!:  :!:   !::  :!:       :!:  !:!  :!:  !:!  :!:  !:!  
 :::: ::   ::   ::: ::::   ::: :::  ::   :::  ::   :::  ::   :::  
:: :  :   :     :: :: :    :: :: :   :   : :   :   : :   :   : :  """)
print("CODED BY ENESXSEC - GHOST SEC.")

url = input("[+] DİG CHAR İÇİN HOST GİR: ")

time.sleep(3)
print(Fore.YELLOW + "[!] DİG CHAR BAŞLIYOR")
print(Fore.RED + "")
time.sleep(2)
os.system("dig")
time.sleep(3)
print(Fore.YELLOW + "[!] DİG ANY")
time.sleep(2)
print(Fore.RED + "")
os.system("dig ANY")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG TTL")
print(Fore.RED + "")
os.system("dig TTL")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG +answer -x")
print(Fore.RED + "")
os.system("dig +answer -x")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG +noall +answer")
print(Fore.RED + "")
os.system("dig +noall +answer")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG +nssearch")
print(Fore.RED + "")
os.system("dig +nssearch")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG -i")
print(Fore.RED + "")
os.system("dig -i")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG +trace")
print(Fore.RED + "")
os.system("dig +trace")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG  +short")
print(Fore.RED + "")
os.system("dig +short")
time.sleep(2)
print(Fore.YELLOW + "[!] DİG SOA")
print(Fore.RED + "")
os.system("dig SOA")
time.sleep(3)
print(Fore.YELLOW + "İŞLEM TAMAMLANDI")
