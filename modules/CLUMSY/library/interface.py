import time
import os
import localization


def screensaver():
    os.system("clear")
    print(localization.view(user_language="system", phrase="screensaver"))
    time.sleep(3)


def notify(user_language):
    pass


def header(user_language):
    print(r"|'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''|")
    print(r"|------------------------- C L U M S Y - Deploy the WEB server with one toe :) ---------------------------|")
    print(f"\_____________________________________ {localization.view('system', 'version program')} ____________________________________/")


def main(user_language):
    print(f"=(1)=> ")


def footer(user_language):
    pass


def user_input():
    pass


def control_panel(user_language):
    while True:
        os.system("clear")
        print(localization.view("system", "description"))
        print(localization.view("system", "info"))
        print(localization.view("system", "menu"))
        print(localization.view("system", "author"))
        user_input()
        break
