#######
#
# Импорт библиотек.
#
#######

import configparser
import os
import pathlib
import time
import appearance
import localization
import languages
import logger
import interface


#######
#
# Системные переменные.
#
#######

# Пути до настроек.
PATH_SYSTEM_SETTINGS = "modules/CLUMSY/configs/system_settings.ini"
PATH_USER_SETTINGS = "modules/CLUMSY/configs/user_settings.ini"


#######
#
# Запуск программы.
#
#######

try:
    # Лог о запуске программы.
    logger.add(languages.get("system", "launch_program"), "log")

    #
    # Проверяем, существует ли файл настроек программы.
    #

    # Лог о проверке.
    logger.add(languages.get("system", "check_file_program_settings"), "log")

    if pathlib.Path(PATH_SYSTEM_SETTINGS).is_file():
        print(PATH_SYSTEM_SETTINGS)
        # Если файл существует.

        # Лог о существовании файла.
        logger.add(languages.get("system", "check_file_program_settings_true"), "log")

        system_settings = configparser.ConfigParser()
        system_settings.read(PATH_SYSTEM_SETTINGS)
    else:
        # Если файла не существует.

        # Лог о не существовании файла.
        raise Exception(logger.add(languages.get("system", "check_file_program_settings_false"), "log"))


    #
    # Проверяем, существует ли файл настроек пользователя.
    #

    USER_LANGUAGE = "ru"
except Exception as Error:
    # Лог об неудачном запуске программы.
    logger.add(f"{languages.get('system', 'launch_program_false')} \n Причина: {Error}", "all")
else:
    # Лог об удачном запуске программы.
    logger.add(languages.get(USER_LANGUAGE, "launch_program_true"), "all")
    
    appearance.control_panel(USER_LANGUAGE)
















exit("Next old code...")
# Создаем исключение.
try:

    # Создаем лог о запуске программы.
    logger.add(text=localization.view(user_language="system", phrase="launch_program"),
               level="logs")

    #
    # Проверка целостности файла настроек из PATH_SETTINGS.
    #

    # Создаем исключение.
    try:

        # Создаем лог о проверке.
        logger.add(text=localization.view(user_language="system", phrase="checking_file_settings"),
                   level="logs")

        #
        # Проверяем, существует ли файл настроек в PATH_SETTINGS.
        #

        # Если файл настроек существует.
        if pathlib.Path(PATH_SETTINGS).is_file():

            # Создаем лог об удачной проверке файла.
            logger.add(text=localization.view(user_language="system", phrase="checking_file_settings_true"),
                       level="logs")

            # Создаем объект настроек.
            settings = configparser.ConfigParser()
            settings.read(PATH_SETTINGS)

            #
            # Получаем из настроек выбранный язык программы.
            #

            # Создаем исключения.
            try:

                # Создаем лог о получении секции языка из настроек.
                logger.add(text=localization.view(user_language="system", phrase="getting_settings_language"),
                           level="logs")

                # Присваиваем переменной значение языка программы.
                language = settings.get("system", "language")

            except Exception as Error:
                # Завершаем программу.
                print(Error)

            else:

                #
                # Значение языка успешно получено, теперь нужно его обработать.
                #

                # Создаем лог об успешном получении секции языка из настроек.
                logger.add(text=localization.view(user_language="system", phrase="getting_settings_language_true"),
                           level="logs")

                # Создаем лог.
                logger.add(text=localization.view(user_language="system", phrase="checking_language"),
                           level="logs")

                # Проверяем количество полученных символов. Если равно 0 - ошибка.
                if len(language) == 0:

                    # Создаем лог о том, что полученное значение не имеет символов.
                    logger.add(
                        text=localization.view(user_language="system", phrase="checking_language_null"),
                        level="logs")

                    # Завершаем программу.

                # Если количество символов больше 0, то отправляем тестовый запрос в localization.
                else:

                    # Создаем лог о том, что секция содержит символы.
                    logger.add(
                        text=localization.view(user_language="system", phrase="checking_language_true"),
                        level="logs")

                    # Создаем лог о проверке существования языка.
                    logger.add(
                        text=localization.view(user_language="system", phrase="checking_language_valid"),
                        level="logs")

                    # Проверяем существует ли такой язык.
                    if localization.check(language):

                        # Создаем лог о существовании языка.
                        logger.add(
                            text=localization.view(user_language="system", phrase="checking_language_valid_true"),
                            level="logs")


                    else:
                        # Создаем лог о не существовании языка.
                        logger.add(
                            text=localization.view(user_language="system", phrase="checking_language_valid_false"),
                            level="logs")

        # Если файл настроек не существует.
        else:
            # Создаем лог об не удачной проверке файла.
            exit(logger.add(text=localization.view(user_language="system", phrase="checking_file_settings_false"),
                            level="all"))

    # Не удалось проверить целостность файла из PATH_SETTINGS или он содержит ошибки.
    except Exception as Error:
        print(Error)

    # Файл исправен и не содержит ошибок, а так же выбранный язык программы корректен.
    else:

        pass

# Программа запущенна с ошибками.
except Exception as Error:
    print(Error)

# Программа прошла все проверки и готова к запуску интерфейса.
else:

    # Запускаем загрузочный экран.
#    appearance.boot_screen(user_language="ru")

    # Запускаем панель управления.
    appearance.control_panel(user_language="ru")
