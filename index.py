import colorama
import os
import subprocess
import time

# Initialize colorama to support ANSI escape sequences for colored output
colorama.init()

def print_startup_sequence():
    # Define colors for different parts of the startup sequence
    colors = [colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.CYAN]

    for color in colors:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(f"{color}Starting Up.", end="\r")
        time.sleep(1)
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(f"{color}Starting Up..", end="\r")
        time.sleep(1)
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(f"{color}Starting Up...", end="\r")
        time.sleep(1)

    # Reset color to default
    print(colorama.Fore.RESET)

    # Execute login.py
    subprocess.run(["python", "login.py"])

# Call the function to print the startup sequence and trigger login.py
print_startup_sequence()
