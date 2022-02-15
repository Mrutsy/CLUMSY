import time
import os
import localization
import update


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


def general(user_language):
    os.system("clear")
    print(localization.view("system", "description"))
    print(localization.view("system", "info"))
    print(localization.view("system", "menu"))
    print(localization.view("system", "author"))

    user_input = input(localization.view(user_language, "input"))

    if int(user_input):
        return user_input
    else:
        return False


def control_panel(user_language):

    while True:
        update.check_github()

        user_input = general(user_language)

        if user_input == "888":
            time.sleep(1)
            print(os.system("git pull"))
            time.sleep(1)
            exit(os.system("sh run.sh"))
            time.sleep(1)
        elif user_input == "999":
            exit("Exited")
        elif user_input == "777":
            time.sleep(3)
            print("OK")
            time.sleep(3)