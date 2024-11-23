from colorama import Fore, Back, Style, init


init()

print(Fore.RED + "червоного кольору.")
print(Fore.GREEN + "зеленого кольору." + Style.RESET_ALL)
print(Back.YELLOW + "із жовтим фоном." + Style.RESET_ALL)
print(Style.BRIGHT + Fore.BLUE + "яскраво-синій текст." + Style.RESET_ALL)
print("після скидання стилів.")
