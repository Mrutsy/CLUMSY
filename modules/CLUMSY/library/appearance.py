import os
import time

import languages


def boot_screen(user_language):
    print(
        f"\n"
        f"                               ____   _      _   _   __  __   ____  __   __ \n"
        f"                              / ___| | |    | | | | |  \/  | / ___| \ \ / / \n"
        f"                             | |     | |    | | | | | |\/| | \___ \  \ V /  \n"
        f"                             | |___  | |___ | |_| | | |  | |  ___) |  | |   \n"
        f"                              \____| |_____\ \___/  |_|  |_| |____/   |_|   \n"
        f"{languages.view(language=user_language, phrase='slogan')}"
        f"\n"
        f"\n|===>     {languages.system('version_program')} | {languages.system('date_program')} | {languages.system('author_program')}     <===|\n"
    )

    time.sleep(0)


def control_panel(user_language):

    # Так как оповещение еще не создано, отключаем его отображение и делаем пустым его код.
    notify = False
    notify_type = None
    notify_code = None

    while True:

        os.system("clear")

        print(
            f"\n"
            f"                               ____   _      _   _   __  __   ____  __   __ \n"
            f"                              / ___| | |    | | | | |  \/  | / ___| \ \ / / \n"
            f"                             | |     | |    | | | | | |\/| | \___ \  \ V /  \n"
            f"                             | |___  | |___ | |_| | | |  | |  ___) |  | |   \n"
            f"                              \____| |_____\ \___/  |_|  |_| |____/   |_|   \n"
            f"{languages.view(language=user_language, phrase='slogan')}"
            f"\n"
            f"\n|===>           {languages.system('version_program')} |"
            f" {languages.system('date_program')} |"
            f" {languages.system('author_program')}           <===|\n"
            f"#                                                                                                    #"
        )

        # Вывод имени и слогана программы.
        #print(
        #    f"#                                                                                                    #\n"
        #    f"#------------------------------------------- C L U M S Y --------------------------------------------#\n"
        #    f"{languages.view(language=user_language, phrase='slogan')}"
        #    f"#----------------------------------------------------------------------------------------------------#\n"
        #    f"#                                                                                                    #"
        #)

        # Если есть оповещение то выводим его.
        if notify:

            if notify_type == "ERROR":
                # Вывод оповещения.
                print(
                    f"{languages.view(language=user_language, phrase='ERROR')}"
                    f"{languages.view(language=user_language, phrase=notify_code)}"
                )

        # Вывод информации о программе.
        print(
            f"#                                                                                                    #\n"
            f"#------------------------------------------- C L U M S Y --------------------------------------------#\n"
            f"{languages.view(language=user_language, phrase='slogan')}"
            f"#----------------------------------------------------------------------------------------------------#\n"
            f"#                                                                                                    #"
        )

        # Вывод меню программы.
        print(
            f"#                                                                                                    #\n"
            f"#------------------------------------------- C L U M S Y --------------------------------------------#\n"
            f"{languages.view(language=user_language, phrase='slogan')}"
            f"#----------------------------------------------------------------------------------------------------#\n"
            f"#                                                                                                    #"
        )

        # Вывод информации о версии и авторе программы.
        #print(
        #    f"#                                                                                                    #\n"
        #    f"#----------------------------------------------------------------------------------------------------#\n"
        #    f"{languages.view(language=user_language, phrase='footer')}"
        #    f"#----------------------------------------------------------------------------------------------------#\n"
        #    f"#                                                                                                    #"
        #)

        # Пользовательский ввод.
        try:

            user_input = int(input(languages.view(language=user_language, phrase='input')))
        except ValueError:
            notify = True
            notify_type = "ERROR"
            notify_code = "ERROR_input_dont_number"
            #print(languages.view(language=user_language, phrase='wrong_input'))
            #time.sleep(5)
        else:
            # Отключаем отображение оповещения, так как оно уже было показано.
            notify = False

            pass
