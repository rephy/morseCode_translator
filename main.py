from translator import Translator

from os import system
from time import sleep
import pyperclip as pc

def clear():

    system("clear")

def wait():

    sleep(3)

def new_line():

    print("\n")

translator = Translator()

while True:
    clear()

    to_or_from = input("Would you like to translate to or from morse code? (to morse code) ").lower().strip()

    clear()

    print("Setting up translator...")
    wait()

    clear()

    if to_or_from == "" or to_or_from == "to morse code":
        to_translate = input("What would you like to translate into morse code? ").lower().strip()

        clear()

        print("Translating...")
        wait()

        clear()

        result = translator.to_morse(to_translate)
        print(f"Your result: {result}")
        wait()
    else:
        to_translate = input("What would you like to translate from morse code? ").lower().strip()

        clear()

        print("Translating...")
        wait()

        clear()

        result = translator.from_morse(to_translate)
        print(f"Your result: {result}")
        wait()

    new_line()

    copy = input("Would you like to copy your result? (yes) ").lower().strip()

    if copy == "" or copy == "yes":
        pc.copy(result)
        new_line()
        print("Result copied to your clipboard.")
        wait()

    clear()

    restart = input("Do you want to run the translator again? (yes) ").lower().strip()

    if restart == "" or restart == "yes":
        clear()

        print("Restarting...")
        wait()

        clear()
    else:
        clear()

        print("Alright then, have a great day!")
        wait()

        break