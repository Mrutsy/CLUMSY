###############################################################################################
# --------------------------------------------------------------------------------------------#
# --------------------------------V: 0.1 ALPHA | D: 18.01.2022--------------------------------#
# --------------------------------Created with ❤ by @zhilllllka-------------------------------#
# ----------------------------------------Made in Russia--------------------------------------#
# --------------------------------------------------------------------------------------------#
###############################################################################################
#
#
#
#
#
##################################################
# ИМПОРТ БИБЛИОТЕК | IMPORTING LIBRARIES | 导入库 #
##################################################
import os

#
#
#
#
#
#######################################
# ЛОКАЛИЗАЦИЯ | LOCALIZATION | 本地化  #
#######################################
#
#
#
localization_base = {
    "ru": {
        'description':
            '#                                                                                             #\n'
            '#--------------------------------------- C L U M S Y -----------------------------------------#\n'
            '#                          Разверни WEB - сервер одним пальцем ноги.                          #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'unknown_action':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                        О Ш И Б К А                                          #\n'
            '#                       Неизвестный пункт меню, повторите, пожалуйста.                        #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'update_interface':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                        У С П Е Х                                            #\n'
            '#                            Интерфейс программы успешно обновлен.                            #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'menu':
            '#                                                                                             #\n'
            '#                                       .:: М Е Н Ю ::.                                       #\n'
            '#                                                                                             #\n'
            '#                        (0) - Обновить интерфейс                                             #\n'
            '#                        (1) - Начать процесс установки компонентов                           #\n'
            '#                        (2) - Начать процесс удаления компонентов                            #\n'
            '#                        (777) - Сменить язык                                                 #\n'
            '#                        (999) - Выйти из программы                                           #\n'
            '#                                                                                             #\n'
            '#                                                                                             #',
        'author':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #\n'
            '#                          Версия: 0.1 АЛЬФА | Дата релиза: 18.01.2022                        #\n'
            '#                               Реализовано с ❤ - @zhilllllka                                 #\n'
            '#                                         Сделано в России                                    #\n'
            '#                                                                                             #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #\n',
        'select_action':
            "Выберите пункт меню (цифра): ",
        "success_out":
            "Программа успешно завершена.\n Спасибо за использование.",
        "installing_components":
            "Добро пожаловать в мастер установки компонентов WEB - сервера.\n"
            "Я помогу Вам установить и настроить WEB - сервер, просто следуйте инструкциями ниже.\n",
        "installing_components_web_server":
            "Давайте выберем с вами ядро WEB - сервера.\n"
            "На данный момент широко используются два ядра - это Apache и Nginx.\n"
            "\n"
            "\n"
            "\n"
            " --- Apache\n"
            "Apache HTTP Server был разработан Робертом Маккулом в 1995 году, \n"
            "а с 1999 года разрабатывается под управлением Apache Software Foundation\n"
            "— фонда развития программного обеспечения Apache. Так как HTTP сервер это\n"
            "первый и самый популярный проект фонда его обычно называют просто Apache.\n"
            "Веб-север Apache был самым популярным веб-сервером в интернете с 1996 года.\n"
            "Благодаря его популярности у Apache сильная документация и интеграция со\n"
            "сторонним софтом. Администраторы часто выбирают Apache из-за его гибкости,\n"
            "мощности и широкой распространенности. Он может быть расширен с помощью системы\n"
            "динамически загружаемых модулей и исполнять программы на большом количестве\n"
            "интерпретируемых языков программирования без использования внешнего\n"
            "программного обеспечения.\n"
            "\n"
            "\n"
            " --- Nginx\n"
            "В 2002 году Игорь Сысоев начал работу над Nginx для того чтобы решить\n"
            "проблему C10K — требование к ПО работать с 10 тысячами одновременных\n"
            "соединений. Первый публичный релиз был выпущен в 2004 году, поставленная\n"
            "цель была достигнута благодаря асинхронной event-driven архитектуре. Nginx\n"
            "начал набирать популярность с момента релиза благодаря своей легковесности\n"
            "(light-weight resource utilization) и возможности легко масштабироваться\n"
            "на минимальном железе. Nginx превосходен при отдаче статического контента\n"
            "и спроектирован так, чтобы передавать динамические запросы другому ПО\n"
            "предназначенному для их обработки. Администраторы часто выбирают Nginx\n"
            "из-за его эффективного потребления ресурсов и отзывчивости под нагрузкой,\n"
            "а также из-за возможности использовать его и как веб-сервер, и как прокси.\n"
            "\n"
            "\n"
            "\n"
            "(0) - Пропустить шаг | (1) - Apache | (2) - Nginx.\n",
        "installing_components_web_server_nginx":
            "Отличный выбор!\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_web_server_apache":
            "Отличный выбор!\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_php":
            "Введите версию php цифрами.\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_db":
            "Какую программу будем использовать в качестве базы данных?\n"
            "(0) - Пропустить шаг | (1) - MySQL | (2) - MongoDB.\n",
        "installing_components_domain":
            "Давайте добавим домен к нашему сайту.\n"
            "(0) - Пропустить шаг | (2) - Его нет (localhost) | (3) - Добавить 1 домен | (4) - Добавить несколько доменов.\n",
        "installing_components_ssl":
            "Какой способ будем использовать для получения SSL?\n"
            "(0) - Пропустить шаг | (1) - CertBot (LetsEncrypt) | (2) - Самоподписанный сертификат.\n",
        "installing_components_input":
            "Выберите цифру из списка - она заключена в скобках (цифра), освободите ее: \n",
        "installing_components_error_input":
            "К сожалению, вы сделали не правильный выбор, повторите, пожалуйста.\n",

    },
    "en": {
        'description':
            '#                                                                                             #\n'
            '#--------------------------------------- C L U M S Y -----------------------------------------#\n'
            '#                             Deploying a web server with one toe.                            #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'unknown_action':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                         E R R O R                                           #\n'
            '#                       Неизвестный пункт меню, повторите, пожалуйста.                        #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'update_interface':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                      S U C C E S S                                          #\n'
            '#                            Интерфейс программы успешно обновлен.                            #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'menu':
            '#                                                                                             #\n'
            '#                                       .:: M E N U ::.                                       #\n'
            '#                                                                                             #\n'
            '#                        (0) - Обновить интерфейс                                             #\n'
            '#                        (1) - Начать процесс установки компонентов                           #\n'
            '#                        (2) - Начать процесс удаления компонентов                            #\n'
            '#                        (777) - Сменить язык                                                 #\n'
            '#                        (999) - Выйти из программы                                           #\n'
            '#                                                                                             #\n'
            '#                                        :: - - - - ::                                        #\n'
            '#                                                                                             #\n'
            '#                                                                                             #',
        'author':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #\n'
            '#                          Version: 0.1 ALPHA | Date release: 18.01.2022                      #\n'
            '#                               Created with ❤ by @zhilllllka                                 #\n'
            '#                                         Made in Russia                                      #\n'
            '#                                                                                             #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #\n',
        'select_action':
            "Выберите пункт меню (цифра): ",
        "success_out":
            "Программа успешно завершена.\n Спасибо за использование.",
        "installing_components":
            "Добро пожаловать в мастер установки компонентов WEB - сервера.\n"
            "Я помогу Вам установить и настроить WEB - сервер, просто следуйте инструкциями ниже.\n",
        "installing_components_web_server":
            "Давайте выберем с вами ядро WEB - сервера.\n"
            "На данный момент широко используются два ядра - это Apache и Nginx.\n"
            "\n"
            "\n"
            "\n"
            " --- Apache\n"
            "Apache HTTP Server был разработан Робертом Маккулом в 1995 году, \n"
            "а с 1999 года разрабатывается под управлением Apache Software Foundation\n"
            "— фонда развития программного обеспечения Apache. Так как HTTP сервер это\n"
            "первый и самый популярный проект фонда его обычно называют просто Apache.\n"
            "Веб-север Apache был самым популярным веб-сервером в интернете с 1996 года.\n"
            "Благодаря его популярности у Apache сильная документация и интеграция со\n"
            "сторонним софтом. Администраторы часто выбирают Apache из-за его гибкости,\n"
            "мощности и широкой распространенности. Он может быть расширен с помощью системы\n"
            "динамически загружаемых модулей и исполнять программы на большом количестве\n"
            "интерпретируемых языков программирования без использования внешнего\n"
            "программного обеспечения.\n"
            "\n"
            "\n"
            " --- Nginx\n"
            "В 2002 году Игорь Сысоев начал работу над Nginx для того чтобы решить\n"
            "проблему C10K — требование к ПО работать с 10 тысячами одновременных\n"
            "соединений. Первый публичный релиз был выпущен в 2004 году, поставленная\n"
            "цель была достигнута благодаря асинхронной event-driven архитектуре. Nginx\n"
            "начал набирать популярность с момента релиза благодаря своей легковесности\n"
            "(light-weight resource utilization) и возможности легко масштабироваться\n"
            "на минимальном железе. Nginx превосходен при отдаче статического контента\n"
            "и спроектирован так, чтобы передавать динамические запросы другому ПО\n"
            "предназначенному для их обработки. Администраторы часто выбирают Nginx\n"
            "из-за его эффективного потребления ресурсов и отзывчивости под нагрузкой,\n"
            "а также из-за возможности использовать его и как веб-сервер, и как прокси.\n"
            "\n"
            "\n"
            "\n"
            "(0) - Пропустить шаг | (1) - Apache | (2) - Nginx.\n",
        "installing_components_web_server_nginx":
            "Отличный выбор!\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_web_server_apache":
            "Отличный выбор!\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_php":
            "Введите версию php цифрами.\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_db":
            "Какую программу будем использовать в качестве базы данных?\n"
            "(0) - Пропустить шаг | (1) - MySQL | (2) - MongoDB.\n",
        "installing_components_domain":
            "Давайте добавим домен к нашему сайту.\n"
            "(0) - Пропустить шаг | (2) - Его нет (localhost) | (3) - Добавить 1 домен | (4) - Добавить несколько доменов.\n",
        "installing_components_ssl":
            "Какой способ будем использовать для получения SSL?\n"
            "(0) - Пропустить шаг | (1) - CertBot (LetsEncrypt) | (2) - Самоподписанный сертификат.\n",
        "installing_components_input":
            "Выберите цифру из списка - она заключена в скобках (цифра), освободите ее: \n",
        "installing_components_error_input":
            "К сожалению, вы сделали не правильный выбор, повторите, пожалуйста.\n",

    },
    "cn": {
        'description':
            '#                                                                                             #\n'
            '#--------------------------------------- C L U M S Y -----------------------------------------#\n'
            '#                          Разверни WEB - сервер одним пальцем ноги.                          #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'unknown_action':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                        О Ш И Б К А                                          #\n'
            '#                       Неизвестный пункт меню, повторите, пожалуйста.                        #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'update_interface':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                        У С П Е Х                                            #\n'
            '#                            Интерфейс программы успешно обновлен.                            #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #',
        'menu':
            '#                                                                                             #\n'
            '#                                       .:: М Е Н Ю ::.                                       #\n'
            '#                                                                                             #\n'
            '#                        (0) - Обновить интерфейс                                             #\n'
            '#                        (1) - Начать процесс установки компонентов                           #\n'
            '#                        (2) - Начать процесс удаления компонентов                            #\n'
            '#                        (777) - Сменить язык                                                 #\n'
            '#                        (999) - Выйти из программы                                           #\n'
            '#                                                                                             #\n'
            '#                                                                                             #',
        'author':
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #\n'
            '#                          Версия: 0.1 АЛЬФА | Дата релиза: 18.01.2022                        #\n'
            '#                               Реализовано с ❤ - @zhilllllka                                 #\n'
            '#                                         Сделано в России                                    #\n'
            '#                                                                                             #\n'
            '#---------------------------------------------------------------------------------------------#\n'
            '#                                                                                             #\n',
        'select_action':
            "Выберите пункт меню (цифра): ",
        "success_out":
            "Программа успешно завершена.\n Спасибо за использование.",
        "installing_components":
            "Добро пожаловать в мастер установки компонентов WEB - сервера.\n"
            "Я помогу Вам установить и настроить WEB - сервер, просто следуйте инструкциями ниже.\n",
        "installing_components_web_server":
            "Давайте выберем с вами ядро WEB - сервера.\n"
            "На данный момент широко используются два ядра - это Apache и Nginx.\n"
            "\n"
            "\n"
            "\n"
            " --- Apache\n"
            "Apache HTTP Server был разработан Робертом Маккулом в 1995 году, \n"
            "а с 1999 года разрабатывается под управлением Apache Software Foundation\n"
            "— фонда развития программного обеспечения Apache. Так как HTTP сервер это\n"
            "первый и самый популярный проект фонда его обычно называют просто Apache.\n"
            "Веб-север Apache был самым популярным веб-сервером в интернете с 1996 года.\n"
            "Благодаря его популярности у Apache сильная документация и интеграция со\n"
            "сторонним софтом. Администраторы часто выбирают Apache из-за его гибкости,\n"
            "мощности и широкой распространенности. Он может быть расширен с помощью системы\n"
            "динамически загружаемых модулей и исполнять программы на большом количестве\n"
            "интерпретируемых языков программирования без использования внешнего\n"
            "программного обеспечения.\n"
            "\n"
            "\n"
            " --- Nginx\n"
            "В 2002 году Игорь Сысоев начал работу над Nginx для того чтобы решить\n"
            "проблему C10K — требование к ПО работать с 10 тысячами одновременных\n"
            "соединений. Первый публичный релиз был выпущен в 2004 году, поставленная\n"
            "цель была достигнута благодаря асинхронной event-driven архитектуре. Nginx\n"
            "начал набирать популярность с момента релиза благодаря своей легковесности\n"
            "(light-weight resource utilization) и возможности легко масштабироваться\n"
            "на минимальном железе. Nginx превосходен при отдаче статического контента\n"
            "и спроектирован так, чтобы передавать динамические запросы другому ПО\n"
            "предназначенному для их обработки. Администраторы часто выбирают Nginx\n"
            "из-за его эффективного потребления ресурсов и отзывчивости под нагрузкой,\n"
            "а также из-за возможности использовать его и как веб-сервер, и как прокси.\n"
            "\n"
            "\n"
            "\n"
            "(0) - Пропустить шаг | (1) - Apache | (2) - Nginx.\n",
        "installing_components_web_server_nginx":
            "Отличный выбор!\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_web_server_apache":
            "Отличный выбор!\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_php":
            "Введите версию php цифрами.\n"
            "(0) - Пропустить шаг.\n",
        "installing_components_db":
            "Какую программу будем использовать в качестве базы данных?\n"
            "(0) - Пропустить шаг | (1) - MySQL | (2) - MongoDB.\n",
        "installing_components_domain":
            "Давайте добавим домен к нашему сайту.\n"
            "(0) - Пропустить шаг | (2) - Его нет (localhost) | (3) - Добавить 1 домен | (4) - Добавить несколько доменов.\n",
        "installing_components_ssl":
            "Какой способ будем использовать для получения SSL?\n"
            "(0) - Пропустить шаг | (1) - CertBot (LetsEncrypt) | (2) - Самоподписанный сертификат.\n",
        "installing_components_input":
            "Выберите цифру из списка - она заключена в скобках (цифра), освободите ее: \n",
        "installing_components_error_input":
            "К сожалению, вы сделали не правильный выбор, повторите, пожалуйста.\n",

    },
}

import pa
#
#
#
#
#
#############################
# ФУНКЦИИ | FUNCTION | 功能  #
#############################
#
#
#
def create_folders(path):
    os.makedirs(path)


def installing_components_nginx():
    create_folders("etc/nginx")
    os.system("sleep 5")


def installing_components_ssl():
    pass


def installing_components():
    user_web_server = None
    user_db = None
    user_php = None
    user_ssl = None
    user_domain = None

    print(localization["installing_components"])

    while True:

        if not user_web_server:
            print(localization["installing_components_web_server"])
            user_web_server = input(localization["installing_components_input"])
            if user_web_server == "0":
                pass
            elif user_web_server == "1":
                print(localization["installing_components_web_server_apache"])
            elif user_web_server == "2":
                print(localization["installing_components_web_server_nginx"])
                installing_components_nginx()
            else:
                print(localization["installing_components_error_input"])
                user_web_server = None
                os.system("sleep 3")
            os.system("clear")
        elif not user_php:
            print(localization["installing_components_php"])
            user_php = input(localization["installing_components_input"])
            if user_php == "0":
                pass
            elif user_php == "2":
                pass
            elif user_php == "3":
                pass
            else:
                print(localization["installing_components_error_input"])
                user_php = None
                os.system("sleep 3")
            os.system("clear")
        elif not user_db:
            print(localization["installing_components_db"])
            user_db = input(localization["installing_components_input"])
            os.system("clear")
        elif not user_domain:
            print(localization["installing_components_domain"])
            user_domain = input(localization["installing_components_input"])
            os.system("clear")
        elif not user_ssl:
            print(localization["installing_components_ssl"])
            user_ssl = input(localization["installing_components_input"])
            os.system("clear")
        else:
            break


#
#
#
#
#
#############################
# ЛОГИКА | LOGIC | 逻辑推理  #
#############################
#
#
#
# Выбор языка.
while True:
    # Просим пользователя выбрать его языковые настройки.
    user_lang = input("(1) [-RU-] Выберите цифру соответствующую Вашему языку\n"
                      "(2) [-EN-] Choose a number corresponding to your language\n"
                      "(3) [-CN-] 选择与您的语言对应的数字\n")
    # Обрабатываем запрос и присваиваем массиву языка выбранное пользователем язык.
    if user_lang == "1":
        localization = localization_base["ru"]
        # Очищаем содержимое окна.
        os.system("clear")
        #
        break
    elif user_lang == "2":
        localization = localization_base["en"]
        # Очищаем содержимое окна.
        os.system("clear")
        #
        break
    elif user_lang == "3":
        localization = localization_base["cn"]
        # Очищаем содержимое окна.
        os.system("clear")
        #
        break
    else:
        os.system("clear")
        print(
            "Сожалею, но Вы выбрали несуществующий вариант языка, пожалуйста, повторите.\n Чтобы выбрать Русский язык, введите 1 а затем нажмите Enter.\n"
            "\nI'm sorry, but you chose a non-existent language option, please repeat.\n To select English, type 2 and then press Enter.\n"
            "\n对不起，但你选择了一个不存在的语言选项，请重复。\n 要选择中文，请键入3，然后按Enter键。\n\n\n")
#
#
# Меню.
error = False
error_code = "False"
while True:
    #
    # Отображаем описание программы.
    print(localization["description"])
    #
    # Отображаем уведомления.
    if error:
        print(localization[error_code])
    #
    # Отображаем программную информацию.
    #
    # Отображаем пункты меню.
    print(localization["menu"])
    #
    # Отображаем авторскую информацию
    print(localization["author"])
    #
    # Получаем пользовательский ввод.
    user_action = input(localization["select_action"])
    #
    # Обрабатываем пользовательский ввод.
    #
    if user_action == "0":
        os.system("clear")
        error = True
        error_code = "update_interface"
    elif user_action == "1":
        os.system("clear")
        error = False
        installing_components()
    elif user_action == "2":
        os.system("clear")
        error = False
    elif user_action == "999":
        os.system("clear")
        exit(localization["success_out"])
    elif user_action == "":
        os.system("clear")
        error = False
    else:
        os.system("clear")
        error = True
        error_code = "unknown_action"