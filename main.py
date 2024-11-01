import random
import string
import time
import sys
import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generate_usernames_or_passwords(option, num_items, length, include_letters=True, include_digits=True):
    characters = ''
    
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits

    if not characters:
        raise ValueError("You must choose letters or digits at least.")

    items = set()
    while len(items) < num_items:
        item = ''.join(random.choices(characters, k=length))
        items.add(item)
    
    return list(items)

while True:
    print(f"""{Fore.BLUE}
          


██████╗ ███████╗██╗   ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗  
██╔══██╗██╔════╝██║   ██║    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██████╔╝█████╗  ██║   ██║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██╔══██╗██╔══╝  ╚██╗ ██╔╝    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║███████╗ ╚████╔╝     ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚══════╝  ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
                                      {Fore.LIGHTCYAN_EX}      {Style.BRIGHT}                 Made by rev  
                                                                                   """)
    slow_print("Welcome to the best User and Password Generator!")
    print()

    
    while True:
        print("What do you want to create ?")
        print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[{Fore.RESET} username {Fore.LIGHTCYAN_EX}{Style.BRIGHT}]")
        print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[{Fore.RESET} password {Fore.LIGHTCYAN_EX}{Style.BRIGHT}]")
        choice = input().strip().lower()
        if choice in ['username', 'password']:
            break
        print(f"{Fore.RED}Invalid choice! Please enter {Fore.RESET}'username' {Fore.RED}or {Fore.RESET}'password'.")

    while True:
        slow_print(f"Enter the number of {choice}s required: ")
        try:
            num_items = int(input().strip())
            if num_items > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter a valid number.")

    
    while True:
        slow_print(f"Enter the length of each {choice}: ")
        try:
            length = int(input().strip())
            if length > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter a valid number.")

    
    while True:
        slow_print("Do you want to include letters? (yes/no): ")
        include_letters = input().strip().lower()
        if include_letters in ['yes', 'no']:
            include_letters = include_letters == 'yes'
            break
        print(f"{Fore.RED}Invalid input! Please enter {Fore.RESET}'yes' {Fore.RED}or {Fore.RESET}'no'.")

    while True:
        slow_print("Do you want to include digits? (yes/no): ")
        include_digits = input().strip().lower()
        if include_digits in ['yes', 'no']:
            include_digits = include_digits == 'yes'
            break
        print(f"{Fore.RED}Invalid input! Please enter {Fore.RESET}'yes' {Fore.RED}or {Fore.RESET}'no'.")

    items = generate_usernames_or_passwords( choice, num_items, length, include_letters, include_digits)

    
    filename = f"{choice}.txt"
    with open(filename, 'w') as file:
        for item in items:
            file.write(item + '\n')

    print(f"Generated {choice}s:")
    for item in items:
        print(Fore.MAGENTA+ item)
    
    print(f"The {choice}s have been saved to {filename}.")

    
    while True:
        slow_print("Do you want to generate more? (yes/no): ")
        restart = input().strip().lower()
        if restart in ['yes', 'no']:
            break
        print(f"{Fore.RED}Invalid input! Please enter {Fore.RESET}'yes' {Fore.RED}or {Fore.RESET}'no'.")

    if restart != 'yes':
        slow_print("Thank you for using rev maker")
        print()
    
        print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Follow me on Instagram for more tools ( @iwvy_ )")
        print()
        break