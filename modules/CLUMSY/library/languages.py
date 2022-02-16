import os


def system(phrase):
    phrases = {
        "version_program":
            "1.0.7 DEV",

        "date_program":
            "16.02.2022",

        "author_program":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author1":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author2":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

        "author3":
            "Created with ❤ by Roman Zhilkin - @zhilllllka",

    }

    if phrases[phrase]:
        return phrases[phrase]
    else:
        return False


def ru(phrase):
    phrases = {
        "slogan":
            f"#                              Разверни WEB - сервер одним пальцем ноги.                             #\n",

        "info_title":
            f"#                                    -----------------------------                                   #\n"
            f"#                                    |--- И Н Ф О Р М А Ц И Я ---|                                   #\n"
            f"#                                    -----------------------------                                   #\n",
        "info_items_status":
            f"#   Статус: \n",

        "menu_title":
            f"#                                          -----------------                                         #\n"
            f"#                                          |--- М Е Н Ю ---|                                         #\n"
            f"#                                          -----------------                                         #\n",
        "menu_items":
            f"#                             (0) - Обновить интерфейс программы                                     #\n"
            f"#                             (1) - Установить компоненты программы                                  #\n"
            f"#                             (2) - Удалить компоненты программы                                     #\n"
            f"#                             (8) - Обновить версию программы                                        #\n"
            f"#                             (9) - Выйти из программы                                               #\n",

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
            f"# ===> Необходимо ввести цифру находящиеся в скобках рядом с пунктом меню.                           #",
    }

    return phrases[phrase]


def en(phrase):
    phrases = {
        "":
            "",
        "slogan":
            f"#                                Deploy the WEB server with one toe.                                 #\n",
    }

    return phrases[phrase]


def cn(phrase):
    phrases = {
        "":
            "",
        "slogan":
            f"#                                      用一个脚趾部署WEB服务器。                                     #\n",
    }

    return phrases[phrase]


def view(language, phrase):
    if language == "ru":
        return ru(phrase)
    elif language == "en":
        return en(phrase)
    elif language == "cn":
        return cn(phrase)
    else:
        return False
