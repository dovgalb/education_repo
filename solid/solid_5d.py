from abc import ABC
from dataclasses import dataclass

"""
Принцип инверсии зависимости.
Наши классы должны зависеть от интерфейсов или абстрактных классов, а не от конкретных классов и функций

"""


# -------------------НЕПРАВИЛЬНАЯ реализация---------------------

#
# @dataclass
# class ModelForm:
#     """Класс нашей модели"""
#     id: int
#     old: int
#     fio: str
#
#
# class MySQL:
#     """Класс через который мы работаем с базой данных"""
#
#     @staticmethod
#     def save(frm: ModelForm):
#         print('Запись формы в БД...')
#
#
# class WebFramework:
#     """Класс, который представляет Веб-фреймворк"""
#
#     @staticmethod
#     def save(frm: ModelForm):
#         db = MySQL()
#         db.save(frm)
#
#
# if __name__ == "__main__":
#     form = ModelForm(1, 30, 'Зубенко Михаил Петрович')
#     web_f = WebFramework()
#     web_f.save(form)


# -------------------ПРАВИЛЬНАЯ реализация---------------------


class IForm(ABC):
    ...


class ISQL(ABC):
    """Интерфейс баз данных"""
    @staticmethod
    def save(frm: IForm):
        print(f'Запись формы "{frm}" в БД')


@dataclass
class ModelForm(IForm):
    """Класс нашей модели"""
    id: int
    old: int
    fio: str


class WebFramework:
    """Класс, который представляет Веб-фреймворк"""

    @staticmethod
    def save(frm: IForm):
        db: ISQL = MySQL()
        db.save(frm)


class MySQL(ISQL):
    """Класс через который мы работаем с базой данных"""

    @staticmethod
    def save(frm: IForm):
        print('Запись формы в БД...')


if __name__ == "__main__":
    form = ModelForm(1, 30, 'Зубенко Михаил Петрович')
    web_f = WebFramework()
    web_f.save(form)