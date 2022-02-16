import os
import languages


def control_panel(user_language):
    # Так как оповещение еще не создано, отключаем его отображение и делаем пустым его код.
    notify = False
    notify_type = None
    notify_code = None

    while True:

        os.system("clear")

        print(
            f"######################################################################################################\n"
            f"#                                                                                                    #\n"
            f"#                             ____   _      _   _   __  __   ____  __   __                           #\n"
            f"#                            / ___| | |    | | | | |  \/  | / ___| \ \ / /                           #\n"
            f"#                           | |     | |    | | | | | |\/| | \___ \  \ V /                            #\n"
            f"#                           | |___  | |___ | |_| | | |  | |  ___) |  | |                             #\n"
            f"#                            \____| |_____\ \___/  |_|  |_| |____/   |_|                             #\n"
            f"{languages.view(language=user_language, phrase='slogan')}"
            f"#                                                                                                    #\n"
            f"#----------------------------------------------------------------------------------------------------#"
            f"\n|===>           {languages.system('version_program')} |"
            f" {languages.system('date_program')} |"
            f" {languages.system('author_program')}           <===|\n"
            f"#----------------------------------------------------------------------------------------------------#\n"

            f"#                                                                                                    #"
        )

        # Если есть оповещение то выводим его.
        if notify:
            # Вывод оповещения.
            print(
                f"{languages.view(language=user_language, phrase=notify_type)}"
                f"{languages.view(language=user_language, phrase=notify_code)}"
            )

        # Вывод информации.
        print(
            f"#                                                                                                    #\n"
            # f"{languages.view(language=user_language, phrase='info_title')}"
            f"#                                                                                                    #\n"
            f"{languages.view(language=user_language, phrase='info_items_status')}"
            f"#                                                                                                    #"
        )

        # Вывод меню.
        print(
            f"#                                                                                                    #\n"
            f"{languages.view(language=user_language, phrase='menu_title')}"
            f"{languages.view(language=user_language, phrase='menu_items')}"
            f"#                                                                                                    #\n"
            f"######################################################################################################\n"
            f"#                                        | Made in Russia |\n"
            f"#                                         ################"
        )

        # Пользовательский ввод.
        try:

            user_input = int(input(languages.view(language=user_language, phrase='input')))
        except ValueError:
            notify = True
            notify_type = "ERROR"
            notify_code = "ERROR_input_dont_number"
        else:
            # Отключаем отображение оповещения, так как оно уже было показано.
            notify = False

            if user_input == 0:
                notify = True
                notify_type = "SUCCESS"
                notify_code = "SUCCESS_update_interface"
            elif user_input == 8:
                print(os.system("git pull"))
                exit(os.system("sh run.sh"))
                notify = True
                notify_type = "SUCCESS"
                notify_code = "SUCCESS_update_interface"
            elif user_input == 9:
                os.system("clear")
                exit(languages.view(language=user_language, phrase='sign_out'))
            else:
                notify = True
                notify_type = "ERROR"
                notify_code = "ERROR_unknown_menu"
