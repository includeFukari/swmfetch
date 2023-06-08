#!/usr/bin/env python3

import colorama
import platform
import getpass
import os
import psutil
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

t = os.popen('uptime -p').read()[:-1]
used_ram = psutil.virtual_memory().used / (1024 * 1024)
total_ram = psutil.virtual_memory().total / (1024 * 1024)

print(f"\n        {Back.MAGENTA}      {Back.RESET}    " + f" {Fore.RED}    os  {Fore.RESET}" + platform.system(), platform.machine())
print(f"      {Back.MAGENTA}      {Back.RESET}      " + f" {Fore.YELLOW}kernel  {Fore.RESET}"  + platform.release())
print(f"  {Back.MAGENTA}            {Back.RESET}    " + f" {Fore.MAGENTA}wizard 󱑷 {Fore.RESET}" + getpass.getuser())
print(f"    {Back.BLACK}  {Back.YELLOW}  {Back.BLACK}  {Back.YELLOW}  {Back.MAGENTA}    {Back.RESET}  " + f" {Fore.GREEN}uptime  {Fore.RESET}" + t)
print(f"    {Back.BLACK}          {Back.RESET}    " + f" {Fore.BLUE}   ram  {Fore.RESET} {round(used_ram)} M /{round(total_ram)} M")
print(f"    {Back.MAGENTA}  {Back.BLACK}    {Back.MAGENTA}    {Back.RESET}    ")
print(f"    {Back.MAGENTA}          {Back.RESET}      " + f"{Back.BLACK}  {Back.RED}  {Back.GREEN}  {Back.YELLOW}  {Back.BLUE}  {Back.MAGENTA}  {Back.CYAN}  {Back.WHITE}  ")
print(f"  {Back.MAGENTA}              {Back.RESET}    " + f"{Back.LIGHTBLACK_EX}  {Back.LIGHTRED_EX}  {Back.LIGHTGREEN_EX}  {Back.LIGHTYELLOW_EX}  {Back.LIGHTBLUE_EX}  {Back.LIGHTMAGENTA_EX}  {Back.LIGHTCYAN_EX}  {Back.LIGHTWHITE_EX}  {Back.RESET}\n")