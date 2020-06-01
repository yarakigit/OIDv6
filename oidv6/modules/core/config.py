#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Глобальный файл настроек
"""


# ######################################################################################################################
# Класс для выделения текста
# ######################################################################################################################
class Color:
    """Класс для выделения текста"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self._green = '\033[92m'  # Зеленый
        self._red = '\033[91m'    # Красный
        self._blue = '\033[94m'   # Синий
        self._bold = '\033[1m'    # Жирный
        self._end = '\033[0m'     # Выход

    # ------------------------------------------------------------------------------------------------------------------
    # Свойства
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def green(self):
        return self._green

    @property
    def red(self):
        return self._red

    @property
    def blue(self):
        return self._blue

    @property
    def bold(self):
        return self._bold

    @property
    def end(self):
        return self._end


# ######################################################################################################################
# Класс для сообщений
# ######################################################################################################################
class Messages(Color):
    """Класс для сообщений"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        super().__init__()  # Выполнение конструктора из суперкласса

        self._metadata = '[{}] Запуск:' \
                         '\n\tАвтор: {}\n\t' \
                         'Email: {}\n\t' \
                         'Сопровождающие: {}\n\t' \
                         'Версия: {}'

        self._format_time = '%Y-%m-%d %H:%M:%S'  # Формат времени

        self._invalid_arguments = '[{}{}{}] Неверные типы аргументов в "{}" ...'

        self._invalid_args = '[{}{}{}] Необходимые значения в командной строке не найдены ...'