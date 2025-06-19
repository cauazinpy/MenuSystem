import time
import os

def clean_screen():
    os.system("cls" if os.name== "nt" else "clear")
def ask_name():
    answer = input("\033[32mWhat is your name? \033[0m")
    print(f"\033[32mHello! Your name is {answer}!\033[0m")

answer1 = str(input("\033[32mWhat is your name:"))
print(f"Hello! Your name is {answer1}")
time.sleep(2)

while True:
    clean_screen() #clean screen every time the menu starts
    print("\033[32m\n====Menu====")
    print("\033[1;37m 1 - Leave\033[0m")
    print("\033[1;37m 2 - Repeat\033[0m")

    choice = input("\033[32mSelect one option: \033[0m")

    if choice == "1":
        print("\033[32mClosing Tab...\033[0m")
        time.sleep(3)
        break

    elif choice == "2":
        ask_name()  # Call function and repeat questions

    else:
        print("\033[31mInvalid option. Please try again.\033[0m")
        
