import os


def system(phrase):
    phrases = {

        "version_program":
            "1.1.1 DEV",

        "date_program":
            "16.02.2022",

        "author_program":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "launch_program":
            "\n\n -----------------------------------------------------------\n"
            "|   Запуск программы."
            " * Launching the program."
            " * 启动程序。|"
            "\n -----------------------------------------------------------\n"
            "~ | - Успешная операция * * ~\n"
            "~ || - Не удачная операция * * ~\n"
            "~ ||| - Предупреждение * * ~\n"
            "~ |||| - Фатальная операция * * ~\n"
            "~ ||||| - Завершение программы * * ~\n"
            "\n",

        "launch_program_false":
            "||||| Программу запустить не удалось.",

        "check_file_program_settings":
            "Проверяю существует ли файл настроек программы."
            " *"
            " *",

        "check_file_program_settings_true":
            "| Файл настроек программы существует."
            " *"
            " *",

        "check_file_program_settings_false":
            "|||| Файл настроек программы не обнаружен."
            " *"
            " *",

        "ended_program":
            " ||||| Завершение программы"
            " *"
            " *",

        "author3":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author3":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author3":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author3":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author3":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author3":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

    }

    if phrase in phrases:
        return phrases[phrase]
    else:
        return False


def ru(phrase):
    phrases = {

        "launch_program_true":
            "Программа успешно запущена!",

        "slogan":
            f"#                              Разверни WEB - сервер одним пальцем ноги.                             #\n",

        "info_title":
            f"#                                    -----------------------------                                   #\n"
            f"#                                    |--- И Н Ф О Р М А Ц И Я ---|                                   #\n"
            f"#                                    -----------------------------                                   #\n",
        "info_items_status":
            f"#   Статус: \n",

        "menu_title":
            f"#                                          |--- М Е Н Ю ---|                                         #\n",
        "menu_items":
            f"#                               --------------------------------------                               #\n"
            f"#                              *   (0) - Обновить                     *                              #\n"
            f"#                              *   (1) - Установить компоненты        *                              #\n"
            f"#                              *   (2) - Удалить компоненты           *                              #\n"
            f"#                              *   (3) - Перезапустить контейнеры     *                              #\n"
            f"#                              *   (4) - Запустить контейнеры         *                              #\n"
            f"#                              *   (5) - Остановить контейнеры        *                              #\n"
            f"#                              *   (6) - Сменить язык                 *                              #\n"
            f"#                              *   (7) - Установить пароль на вход    *                              #\n"
            f"#                              *   (8) - Обновить программу           *                              #\n"
            f"#                              *   (9) - Выйти                        *                              #\n"
            f"#                               --------------------------------------                               #\n",

        "input":
            f"#\n"
            f"# =====> Введите значение находящиеся в скобке: ",
        "wrong_input":
            f"Необходимо ввести цифру которая соответствует значению. \n"
            f"Например, если вы хотите обновить программу, то нужно ввести 888 и нажать Enter.",

        "SUCCESS":
            f"# =====> УСПЕШНО                                                                                     #\n",
        "SUCCESS_update_interface":
            f"# ===> Интерфейс программы обновлен.                                                                 #",
        "ERROцR_input_dont_number":
            f"# ===> Необходимо ввести цифру находящиеся в скобках рядом с пунктом меню.                           #",

        "ERROR":
            f"# =====> ОШИБКА                                                                                      #\n",
        "ERROR_unknown_menu":
            f"# ===> Неизвестный пункт меню                                                                        #",
        "ERROR_input_dont_number":
            f"# ===> Необходимо ввести цифру находящиеся в скобках рядом с пунктом меню.                          #",

        "sign_out":
            f"Вы успешно вышли!\n"
            f"Спасибо за использование программы.\n"
            f"{system('author_program')}",
    }

    if phrase in phrases:
        return phrases[phrase]
    else:
        return False


def change():
    pass


def check_phrase(language, phrase):
    if language == "system":
        getting_phrase = system(phrase)
    elif language == "ru":
        getting_phrase = ru(phrase)
    else:
        return f"|| Не удалось обнаружить языковой пакет: {language}"

    if getting_phrase:
        return getting_phrase
    else:
        return f"|| Не удалось обнаружить фразу в языковом пакете: {language} | {phrase}"


# Получить фразу из языка.
def get(language, phrase):

    phrase = check_phrase(language, phrase)

    if phrase:
        return phrase
    else:
        return False
