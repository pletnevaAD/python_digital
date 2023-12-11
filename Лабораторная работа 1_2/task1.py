import doctest


class Car:
    def __init__(self, color: str, brand: str, mileage: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param color: Цвет автомобиля
        :param brand: Марка автомобиля
        :param distance: Пробег

        Примеры:
        >>> car = Car('red', 'Kia', 123.1)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет машины должен быть str")
        if 0 > len(color) >= 20:
            raise ValueError("Название цвета должно содержать от 1 до 20 символов")
        self.color = color

        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть str")
        if 0 > len(brand) >= 40:
            raise ValueError("Название марки автомобиля должно содержать от 1 до 40 символов")
        self.brand = brand

        if not isinstance(mileage, (int, float)):
            raise TypeError("Пробег автомобиля должен быть int или float")
        if mileage < 0:
            raise ValueError("Пробег автомобиля должен быть положительным числом")
        self.mileage = mileage

    def get_car_info(self) -> str:
        """
        Функция, которая возвращает информацию об автомобиле в виде строки

        :return: Строка, собержащая полную информацию об автомобиле

        Примеры:
        >>> car = Car('red', 'Kia', 123.1)
        >>> car.get_car_info()
        """
        ...

    def twist_the_mileage(self, mileage: float) -> None:
        """
        Функция, позволяющая скрутить пробег.
        :param mileage: Количество скрученного пробега

        :raise ValueError: Если количество запрашиваемого пробега не положительное число или превышает текущий пробег,
        то вызываем ошибку

        :raise TypeError: Если запрашиваемый пробег не int или float, то вызываем ошибку

        Примеры:
        >>> car = Car('red', 'Kia', 123.1)
        >>> car.twist_the_mileage(100)
        """
        if not isinstance(mileage, (int, float)):
            raise TypeError("Запрашиваемый пробег автомобиля должен быть int или float")
        if mileage < 0:
            raise ValueError("Запрашиваемый пробег автомобиля должен быть положительным числом")
        if mileage > self.mileage:
            raise ValueError("Запрашиваемый пробег автомобиля не должен превышать текущий пробег")
        ...

    def add_mileage(self, mileage: float) -> None:
        """
        Добавление пробега.

        :param mileage: Объем извлекаемой жидкости

        :raise ValueError: Если количество запрашиваемого пробега не положительное число, то вызываем ошибку

        :raise TypeError: Если запрашиваемый пробег не int или float, то вызываем ошибку

        Примеры:
        >>> car = Car('red', 'Kia', 123.1)
        >>> car.add_mileage(200)
        """
        if not isinstance(mileage, (int, float)):
            raise TypeError("Запрашиваемый пробег автомобиля должен быть int или float")
        if mileage < 0:
            raise ValueError("Запрашиваемый пробег автомобиля должен быть положительным числом")
        ...


class Point:
    def __init__(self, x_coord: float, y_coord: float):
        """
        Создание и подготовка к работе объекта "Точка"

        :param x_coord: координата по оси абсцисс
        :param y_coord: координата по оси ординат

        Примеры:
        >>> point = Point(1, 2)  # инициализация экземпляра класса
        """
        if not isinstance(x_coord, (int, float)):
            raise TypeError("Координата x должна быть типа int или float")
        self.x_coord = x_coord

        if not isinstance(y_coord, (int, float)):
            raise TypeError("Координата y должна быть типа int или float")
        self.y_coord = y_coord

    def move(self, d_x: float, d_y: float) -> None:
        """
        Перемещение точки.

        :param d_x: Перемещение по оси абсцисс
        :param d_y: Перемещение по оси ординат

        :raise TypeError: Если перемещение по какой-либо из координат не int или float, то вызываем ошибку

        Примеры:
        >>> point = Point(1, 2)
        >>> point.move(10, -2)
        """
        if not isinstance(d_x, (int, float)):
            raise TypeError("Перемещение по координате x должно быть типа int или float")
        if not isinstance(d_y, (int, float)):
            raise TypeError("Перемещение по координате y должно быть типа int или float")
        ...

    def distance(self, point: 'Point') -> float:
        """
        Перемещение точки.

        :param point: Точка, расстояние до которой мы ищем

        :raise TypeError: Если point не является экземпляром класса Point, то вызываем ошибку

        :return: Расстояние между двумя точками

        Примеры:
        >>> point_1 = Point(1, 2)
        >>> point_2 = Point(2, 3)
        >>> point_1.distance(point_2)
        """
        if not isinstance(point, Point):
            raise TypeError("point должен являться экземпляром класса Point")
        ...

    def get_point_info(self) -> str:
        """
        Функция, которая возвращает информацию о точке в виде строки

        :return: Координаты x и y точки

        Примеры:
        >>> point = Point(3 , 3)
        >>> point.get_point_info()
        """
        ...


class MusicPlayer:
    def __init__(self, brand: str, songs: dict[str, list[str]]):
        """
        Создание и подготовка к работе объекта "Музыкальный плеер"

        :param brand: Бренд плеера
        :param songs: Словарь, содержащий исполнителей в качестве ключей и список песен в качестве значений

        Примеры:
        >>> player = MusicPlayer('Sony', {'The Beatles': ['Help']})  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд плеера должен быть строкой")
        if 0 > len(brand) >= 20:
            raise ValueError("Название бренда плеера должно содержать от 1 до 20 символов")
        self.brand = brand

        if not isinstance(songs, dict):
            raise TypeError("Список песен должен быть словарем")
        for key, value in songs.items():
            if not isinstance(key, str):
                raise TypeError("Исполнитель должен быть строкой")
            if 0 > len(key) >= 40:
                raise ValueError("Имя исполнителя должно содержать от 1 до 40 символов")
            if not isinstance(value, list):
                raise TypeError("Песни исполнителя должны быть списком")
            for song in value:
                if not isinstance(song, str):
                    raise TypeError("Песни в списке должны быть строками")
                if 0 > len(key) >= 100:
                    raise ValueError("Песня должна содержать от 1 до 100 символов")
        self.songs = songs

    def add_new_songs(self, songs: dict[str, list[str]]) -> None:
        """
        Добавление новых песен.

        :param songs: Словарь, содержащий новые песни

        :raise TypeError: Если songs не является словарем, какой либо из ключей словаря не является строкой,
        значением словаря является не list или в списке лежат не строки, то вызываем ошибку
        :raise ValueError: Если строка с исполнителем имеет не от 1 до 40 символов или строки с песнями имеют
        не от 1 до 100 символов, то вызываем ошибку

        Примеры:
        >>> player = MusicPlayer('Sony', {'The Beatles': ['Help']})
        >>> player.add_new_songs({'Kiss': ['Lick It Up']})
        """
        if not isinstance(songs, dict):
            raise TypeError("Список песен должен быть словарем")
        for key, value in songs.items():
            if not isinstance(key, str):
                raise TypeError("Исполнитель должен быть строкой")
            if 0 > len(key) >= 40:
                raise ValueError("Имя исполнителя должно содержать от 1 до 40 символов")
            if not isinstance(value, list):
                raise TypeError("Песни исполнителя должны быть списком")
            for song in value:
                if not isinstance(song, str):
                    raise TypeError("Песни в списке должны быть строками")
                if 0 > len(key) >= 100:
                    raise ValueError("Песня должна содержать от 1 до 100 символов")
        ...

    def delete_song(self, songs: dict[str, list[str]]) -> None:
        """
        Удаление песен.

        :param songs: Словарь, содержащий песни, которые нужно удалить

        :raise TypeError: Если songs не является словарем или значением словаря является не list, то вызываем ошибку
        :raise ValueError: Если песни нет в плеере, то вызываем ошибку

        Примеры:
        >>> player = MusicPlayer('Sony', {'The Beatles': ['Help']})
        >>> player.delete_song({'The Beatles': ['Help']})
        """
        if not isinstance(songs, dict):
            raise TypeError("Список песен должен быть словарем")
        for key, value in songs.items():
            if key not in self.songs.keys():
                raise ValueError("Песен этого исполнителя нет в плеере")
            if not isinstance(value, list):
                raise TypeError("Песни исполнителя должны быть списком")
            for song in value:
                if song not in self.songs[key]:
                    raise ValueError(f"Песни {song} нет в плеере")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
