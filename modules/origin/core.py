import os
import time


class Logging:
    pass


class Phrases:

    def sys(self):
        array = {
            "loading":
                "                                 ____   _      _   _   __  __   ____  __   __                           \n"
                "                                / ___| | |    | | | | |  \/  | / ___| \ \ / /                           \n"
                "                               | |     | |    | | | | | |\/| | \___ \  \ V /                            \n"
                "                               | |___  | |___ | |_| | | |  | |  ___) |  | |                             \n"
                "                                \____| |_____\ \___/  |_|  |_| |____/   |_|                             \n"
                "\n"
        }

        return array[self]

    def ru(self, version="v: 1.0.0.5 DEV | d: 21.03.2022"):
        array = {
            "loading":
                "Загрузка...",
            "header":
                f'#                                                                                                    #\n'
                f'#-------------------------------------------- C L U M S Y -------------------------------------------#\n'
                f'#                               Разверни WEB - сервер одним пальцем ноги.                            #\n'
                f'#----------------------------------------------------------------------------------------------------#\n'
                f'#                                                                                                    #',
            "main-info":
                f"#                                                                                                    #\n"
                f"#                                    |--- И Н Ф О Р М А Ц И Я ---|                                   #\n"
                f"#                                                                                                    #",
            "main-menu":
                f"#                                          |--- М Е Н Ю ---|                                         #\n"
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
                f"#                               --------------------------------------                               #",
            "footer":
                f'#----------------------------------------------------------------------------------------------------#\n'
                f'#                   {version} | Создано с ❤ - @zhilllllka                       #\n'
                f'#----------------------------------------------------------------------------------------------------#\n'
                f'#                                                                                                    #',
            "input":
                f"#\n"
                f"# =====> Введите значение находящиеся в скобке: ",
        }

        return array[self]

    def cn(self, phrase):
        pass

    def en(self, phrase):
        pass

    @staticmethod
    def get(language, phrase):

        if language == "sys":
            return Phrases.sys(phrase)
        elif language == "ru":
            return Phrases.ru(phrase)
        else:
            pass


class Interface:

    @staticmethod
    def show(language, section):

        if section == "loading":
            os.system("clear")
            print(Phrases.get(language, "loading"))
        elif section == "header":
            os.system("clear")
            print(Phrases.get(language, "header"))
        elif section == "main-info":
            print(Phrases.get(language, "main-info"))
        elif section == "main-menu":
            print(Phrases.get(language, "main-menu"))
        elif section == "footer":
            print(Phrases.get(language, "footer"))
        elif section == "start":
            Interface.show("sys", "loading")
            time.sleep(1)
            Interface.show(language, "header")
            Interface.show(language, "main-info")
            Interface.s
            how(language, "main-menu")
            Interface.show(language, "footer")
            Interface.show(language, "input")
            # Interface.show(language, "input"}


Interface.show("ru", "start")
