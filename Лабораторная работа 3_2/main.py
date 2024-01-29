# Есть два типа книг - бумажная и аудио.
# Для всех типов хранения книг у них есть:
#     - название (`name`)
#     - автор (`author`)
#
# У бумажной книги есть количество страниц (`pages`) целочисленного типа данных.
# У аудио книги есть её продолжительность (`duration`) как числа с плавающей запятой.
#
# 1. Для классов `Book`, `PaperBook`, `AudioBook` примените наследование.
# 1. Исходя из кода подумайте когда методы `__str__` и `__repr__` могут быть унаследованы,
# а когда перегружены в дочерних классах. И исправьте это
# 1. Атрибуты `name` и `author` изменяться не могут, поэтому напишите для них свойства, которые не позволят изменять эти атрибуты.
# 1. Так как на `pages` и `duration` накладываются ограничения по типу и допустимым
# значениям, напишите для них свойства с проверками при присвоении им значений.
#

class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError('pages must be int')
        if pages < 0:
            raise ValueError('pages can not be negative')
        self._pages = pages

    def __str__(self):
        return f"{super().__str__()}. Количество страниц - {self.pages}."

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError('duration must be float')
        if duration < 0:
            raise ValueError('duration can not be negative')
        self._duration = duration

    def __str__(self):
        return f"{super().__str__()}. Длительность - {self.duration}."

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, duration={self.duration})"
