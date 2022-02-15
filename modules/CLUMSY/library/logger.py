import os
from datetime import *


def create_log(text):
    path = f"modules/CLUMSY/logs/"

    try:
        log = open(f"{path}/{datetime.today().strftime('%d-%m-%Y')}.log", "a+")
    except FileNotFoundError:
        os.makedirs(path)
        create_log(text)
    else:
        now = datetime.now()
        log.write(f"{now.strftime('%H:%M:%S')} - {text}\n")
        log.close()


def add(text, level):

    # Отладка
    level = "all"

    if level == "logs":
        create_log(text=text)
    elif level == "user":
        now = datetime.now()
        print(f"{now.strftime('%H:%M:%S')} - {text}")
    elif level == "all":
        create_log(text=text)
        print(text)
