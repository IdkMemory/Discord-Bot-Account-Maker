import requests
import colorama
from colorama import Fore, Style
import random


text = f"""{Style.BRIGHT}
----------------------------------------------
{Fore.MAGENTA}______       _    ___  ___      _             
| ___ \     | |   |  \/  |     | |            
| |_/ / ___ | |_  | .  . | __ _| | _____ _ __ 
| ___ \/ _ \| __| | |\/| |/ _` | |/ / _ \ '__|
| |_/ / (_) | |_  | |  | | (_| |   <  __/ |   
\____/ \___/ \__| \_|  |_/\__,_|_|\_\___|_|   
                                              
{Fore.WHITE}----------------------------------------------

"""







print(text)

print(Style.DIM + Fore.YELLOW + "[!] " + Fore.WHITE + "Created by Vexxly\n")

amount = input(Style.NORMAL + Style.BRIGHT + Fore.MAGENTA + "[!] "+ Fore.WHITE + "How Many Bots Do You Want? ")
amount = int(amount)

token = input(f"{Fore.MAGENTA}[!] {Fore.WHITE}Your token: ")

for x in range(amount):
  names = open('names.txt').read().splitlines()
  name =random.choice(names)
  bios = open('bios.txt').read().splitlines()
  bio = random.choice(bios)
  url = "https://discord.com/api/applications"


  payload = {
      "name": name,
      "description": bio,
      "flags": 3276799
  }


  headers = {
      "Authorization": token
  }

  r = requests.post(url, json=payload, headers=headers)
  
  if r.status_code == 201:
      data = r.json()
      id = data['id']
      print(f"{Fore.GREEN}[+] {Fore.WHITE}Created Bot: {id}")
      print(f"{Fore.GREEN}[+] {Fore.WHITE}Successfully Added Bio")
      print(f"{Fore.GREEN}[+] {Fore.WHITE}Successfully Created Bot")

      token_url = f"https://discord.com/api/applications/{id}/bot/reset"
      headers = {
      "Authorization": token
      }
      r2 = requests.post(token_url, headers=headers)
      token = r2.json()['token']
      with open("created/tokens.txt", "a") as myfile:
        myfile.write(token + "\n")
      with open("created/ids.txt", "a") as myfile:
        myfile.write(id + "\n")
  else:
      print(f"{Fore.RED}[-] {Fore.WHITE}Failed to create {name}. Status code: {r.status_code}")
