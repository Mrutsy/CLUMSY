import time
import os
import localization
import update
import shutil


def show(language, section):

    if section == "logo":

        # LOGO.
        print(
            f"######################################################################################################\n"
            f"#                                                                                                    #\n"
            f"#                             ____   _      _   _   __  __   ____  __   __                           #\n"
            f"#                            / ___| | |    | | | | |  \/  | / ___| \ \ / /                           #\n"
            f"#                           | |     | |    | | | | | |\/| | \___ \  \ V /                            #\n"
            f"#                           | |___  | |___ | |_| | | |  | |  ___) |  | |                             #\n"
            f"#                            \____| |_____\ \___/  |_|  |_| |____/   |_|                             #",)

    elif section == "version":
        # Загрузочный экран.
        pass
    elif section == "notification":
        # Загрузочный экран.
        pass
    elif section == "start":
        os.system("clear || cls")
        show(language, "logo")
        print(f"#                                                                                                    #\n"
              f"######################################################################################################\n",)
        time.sleep(3)


def screensaver():
    os.system("clear")
    print(localization.view(user_language="system", phrase="screensaver"))
    time.sleep(3)


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

        if user_input == "0":
            # Обновить интерфейс программы.
            pass

        elif user_input == "1":
            pass

        elif user_input == "2":
            pass

        elif user_input == "3":
            pass

        elif user_input == "4":
            pass

        elif user_input == "888":
            # Обновить версию программы.
            print(os.system("git pull"))
            exit(os.system("sh run.sh"))

        elif user_input == "999":
            # Выйти из программы.
            exit("Завершение программы")

        elif user_input == "123":
            # Пасхальное сообщение.
            exit("Пасхальное сообщение")
