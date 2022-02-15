#!/bin/bash

localization()
{

  # Русская локализация.
  if [ "$1" = "ru" ]; then

      if [ "$2" = "check_python" ]; then
          echo "Проверяю установлен ли Python и поддерживается ли его версия программой.";
      elif [ "$2" = "check_python_true" ]; then
          echo " - Python - установлен и его версия поддерживается программой.
          ";
      elif [ "$2" = "check_python_false" ]; then
          echo " - Python не установлен или версия Python не поддерживается программой.
          Текущая версия: $4
          Необходимо: $6
          "

      elif [ "$2" = "check_git" ]; then
          echo "Проверяю установлен ли Git и поддерживается ли его версия программой.";
      elif [ "$2" = "check_git_true" ]; then
          echo " - Git - установлен и его версия поддерживается программой.
          ";
      elif [ "$2" = "check_git_false" ]; then
          echo " - Git не установлен или версия Git не поддерживается программой.
          Текущая версия: $5
          Необходимо: $8
          "

      elif [ "$2" = "dont_install" ]; then
          echo "ОШИБКА: Для установки программы необходимо устранить проблемы перечисленные выше."
      fi

  # Английская локализация.
  elif [  "$1" = "en"  ]; then

      if [ "$2" = "check_python" ]; then
          echo "Язык пока не поддерживается.";
      elif [ "$2" = "check_python" ]; then
          echo "";
      fi

  # Китайская локализация.
  elif [  "$1" = "cn"  ]; then

      if [ "$2" = "check_python" ]; then
          echo "Язык пока не поддерживается.";
      elif [ "$2" = "check_python" ]; then
          echo "";
      fi
  fi
}


# Узнаем язык пользователя.

while :
do

  clear

  echo "(1) - RU - Введите цифру 1, что бы продолжить на Русском языке и нажмите Enter."
  echo "(2) - EN - Enter the number 2 to continue in English and press Enter."
  echo "(3) - CN - 输入数字3以中文继续，然后按Enter键。"

  read user_language

  if [ "$user_language" = "1" ];
    then
      user_language="ru"
      break
  elif [ "$user_language" = "2" ];
    then
      user_language="en"
      break
  elif [ "$user_language" = "3" ];
    then
      user_language="cn"
      break
  else

    clear

    echo " -RU- Язык не доступен или Вы выбрали не существующий языковой пакет."
    echo " -EN- The language is not available or you have selected a language pack that does not exist."
    echo " -CN- 语言不可用，或者您选择了不存在的语言包。"

    sleep 3

  fi

done



# (RU) - Проверяем, установлен ли в системе Python.

PATH_PYTHON=$(which python3)
VERSION_PYTHON=$($PATH_PYTHON --version)
TRUE_VERSION_PYTHON="Python 3.10.2"

clear
localization $user_language "check_python"

if [ "$VERSION_PYTHON" = "$TRUE_VERSION_PYTHON" ]
then
  localization $user_language "check_python_true"
  check_python="valid"
else
  localization $user_language "check_python_false" $VERSION_PYTHON $TRUE_VERSION_PYTHON
fi



# (RU) - Проверяем установлен ли Git в системе.

PATH_GIT=$(which git)
VERSION_GIT=$($PATH_GIT --version)
TRUE_VERSION_GIT="git version 2.35.1"

localization $user_language "check_git"

if [ "$VERSION_GIT" = "$TRUE_VERSION_GIT" ]
then
  localization $user_language "check_git_true"
  check_git="valid"
else
  localization $user_language "check_git_false" $VERSION_GIT $TRUE_VERSION_GIT
fi

if [ "$check_python" = "valid" ] &&  [ "$check_git" = "valid" ]; then

  git clone https://github.com/zhilllllka/CLUMSY.git -b latest CLUMSY
  rm -f ./install_windows.cmd
  rm -f ./install_macos.scpt
  rm -f ./install_linux.sh
  rm -f ./LICENSE
  rm -f ./README.md
  cd CLUMSY
  sh run.sh
  
else
  localization $user_language "dont_install"
fi
