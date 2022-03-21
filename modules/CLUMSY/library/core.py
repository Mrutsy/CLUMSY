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


"""
-RU-
Перед запуском интерфейса программы, необходимо проверить наличие файлов конфигураций.
    Если файлы существуют, то необходимо считать с них информацию.
    Если нет, то создать эти файлы.
"""

interface.show(language="ru", section="start")


# try:
# Лог о запуске программы.
#    logger.add(languages.get("system", "launch_program"), "log")

#
# Проверяем, существует ли файл настроек программы.
#

# Лог о проверке.
#    logger.add(languages.get("system", "check_file_program_settings"), "log")

#    if path lib.Path(PATH_SYSTEM_SETTINGS).is_file():
# Если файл существует.

# Лог о существовании файла.
#        logger.add(languages.get("system", "check_file_program_settings_true"), "log")

#        system_settings = configparser.ConfigParser()
#        system_settings.read(PATH_SYSTEM_SETTINGS)
#    else:
# Если файла не существует.

# Лог о не существовании файла.
#        raise Exception(logger.add(languages.get("system", "check_file_program_settings_false"), "log"))

#
#    # Проверяем, существует ли файл настроек пользователя.
#

# Лог о проверке.
#    logger.add(languages.get("system", "check_file_user_settings"), "log")

#    if path lib.Path(PATH_USER_SETTINGS).is_file():
# Если файл существует.

# Лог о существовании файла.
#        logger.add(languages.get("system", "check_file_user_set2tings_true"), "log")

#        user_settings = configparser.ConfigParser()
#        user_settings.read(PATH_USER_SETTINGS)
#    else:
# Если файла не существует.

# Лог о не существовании файла.
#        raise Exception(logger.add(languages.get("system", "check_file_user_settings_false"), "log"))

#
# Получаем язык пользователя.
#

# Лог о получении языкового пакета.
#    logger.add(languages.get("system", "getting_user_language"), "log")

#    USER_LANGUAGE = user_settings.get("system", "language")

#    if languages.check(USER_LANGUAGE):
#        pass
#    else:

# Лог о не существовании файла.
#        raise Exception(logger.add(languages.get("system", "check_file_program_settings_false"), "log"))

#
# Проверяем, нужна ли первоначальная настройка.
#

#    installed_program = user_settings.get("system", "installed_program")

#    if installed_program:
#        print("ok")
#    else:
#        print(2)

# except Exception as Error:
# Лог об неудачном запуске программы.
#    logger.add(f"{languages.get('system', 'launch_program_false')} \n Причина: {Error}", "all")
# else:
# Лог об удачном запуске программы.
#    logger.add(languages.get(USER_LANGUAGE, "launch_program_true"), "all")

# appearance.control_panel(USER_LANGUAGE)
