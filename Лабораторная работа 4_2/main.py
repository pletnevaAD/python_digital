import re


class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        """
        Создание и подготовка к работе объекта "Пользователь"

        :param name: Имя
        :param email: Адрес электронной почты
        :param password: Пароль, недоступен для чтения
        """
        self.name = name
        self.email = email
        self.password = password

    @property
    def name(self) -> str:
        """
        Доступ к атрибуту name
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Установка имени.

        :param name: Имя

        :raise TypeError: Если имя не str, то вызываем ошибку
        """
        if not isinstance(name, str):
            raise TypeError('name must be str')
        self._name = name

    @property
    def email(self) -> str:
        """
        Доступ к атрибуту email
        """
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        """
        Установка email.

        :param email: Адрес электронной почты

        :raise TypeError: Если email не str, то вызываем ошибку
        :raise ValueError: Если email невалидный, то вызываем ошибку
        """
        if not isinstance(email, str):
            raise TypeError('email must be str')
        if not self.validate_email(email):
            raise ValueError('invalid email format')
        self._email = email

    @staticmethod
    def validate_email(email) -> bool:
        """
        Проверка валидности email.

        :param email: Адрес электронной почты

        :return: является ли адрес валидным
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @property
    def password(self) -> None:
        """
        Доступ к атрибуту password для чтения закрыт.

        :raise AttributeError: При попытке чтения пароля вызываем ошибку

        """
        raise AttributeError("password is write-only")

    @password.setter
    def password(self, password: str) -> None:
        """
        Установка пароля.

        :param password: Пароль

        :raise TypeError: Если пароль не str, то вызываем ошибку
        """
        if not isinstance(password, str):
            raise TypeError('password must be str')
        self._password = password

    def greeting(self) -> str:
        """
        Выводит приветствие.
        """
        return f'{self.name}, добро пожаловать в профиль!'

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта
        """
        return f"Name: {self.name}\nEmail: {self.email}"

    def __repr__(self) -> str:
        """
        Возвращает представление объекта в виде строки, не выводит атрибут password, так как он не доступен для чтения.

        :return: Представление объекта в виде строки
        """
        return f"{self.__class__.__name__}(name={self.name!r}, email={self.email!r})"


class Administrator(User):
    def __init__(self, name: str, email: str, password: str, age: int, task_list: list[str]) -> None:
        """
        Создание и подготовка к работе объекта "Администратор"

        :param name: Имя
        :param email: Адрес электронной почты
        :param password: Пароль, недоступен для чтения
        :param age: Возраст
        :param task_list: Список задач
        """
        super().__init__(name, email, password)
        self.age = age
        self.task_list = task_list

    @property
    def task_list(self) -> list[str]:
        """
        Доступ к атрибуту task_list
        """
        return self._task_list

    @task_list.setter
    def task_list(self, task_list: list[str]) -> None:
        """
        Установка списка задач.

        :param task_list: Список задач

        :raise TypeError: Если task_list не является списком или задача не является строкой, вызывается ошибка
        """
        if not isinstance(task_list, list):
            raise TypeError('task_list must be list')
        for task in task_list:
            if not isinstance(task, str):
                raise TypeError('task from task_list must be str')
        self._task_list = task_list

    @property
    def age(self) -> int:
        """
        Доступ к атрибуту age
        """
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """
        Установка возраста.

        :param age: Возраст

        :raise TypeError: Если возраст не является целым числом, вызывается ошибка
        """
        if not isinstance(age, int):
            raise TypeError('age must be int')
        self._age = age

    def add_task(self, task: str) -> None:
        """
        Добавить задачу в список.

        :param task: Задача

        :raise TypeError: Если задача не является строкой, вызывается ошибка
        """
        if not isinstance(task, str):
            raise TypeError('task must be str')
        self._task_list.append(task)

    def delete_task(self, task) -> None:
        """
        Удалить задачу из списка.

        :param task: Задача

        :raise TypeError: Если задача не является строкой, вызывается ошибка
        :raise ValueError: Если задачи нет в списке, вызывается ошибка
        """
        if not isinstance(task, str):
            raise TypeError('task must be str')
        if task not in self._task_list:
            raise ValueError('there is no such task in the task list')
        self._task_list.remove(task)

    def greeting(self) -> str:
        """
        Перегруженный метод базового класса, возвращает приветствие администратора.

        :return: Приветствие
        """
        return super().greeting() + ' администратора!'

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта
        """
        return f"{super().__str__()}\nСписок заданий:{self._task_list}."

    def __repr__(self) -> str:
        """
        Возвращает представление объекта в виде строки, не выводит атрибут password, так как он не доступен для чтения.

        :return: Представление объекта в виде строки
        """
        return f"{super().__repr__()[:-1]}, task_list={self._task_list})"


class Client(User):

    def __init__(self, name: str, email: str, password: str, shop_cart: list[str]) -> None:
        """
       Создание и подготовка к работе объекта "Клиент"

       :param name: Имя
       :param email: Адрес электронной почты
       :param password: Пароль, недоступен для чтения
       :param shop_cart: Корзина с товарами
       """
        super().__init__(name, email, password)
        self.shop_cart = shop_cart

    @property
    def shop_cart(self) -> list[str]:
        """
        Доступ к атрибуту shop_cart
        """
        return self._shop_cart

    @shop_cart.setter
    def shop_cart(self, shop_cart: list[str]) -> None:
        """
        Установка корзины с товарами.

        :param shop_cart: Корзина с товарами

        :raise TypeError: Если корзина с товарами не является списком или товар не является строкой, вызывается ошибка
        """
        if not isinstance(shop_cart, list):
            raise TypeError('shop_cart must be list')
        for item in shop_cart:
            if not isinstance(item, str):
                raise TypeError('item from shop_cart must be str')
        self._shop_cart = shop_cart

    def add_item(self, item: str) -> None:
        """
        Добавить товар в корзину.

        :param item: Название товара

        :raise TypeError: Если товар не является строкой, вызывается ошибка
        """
        if not isinstance(item, str):
            raise TypeError('item must be str')
        self._shop_cart.append(item)

    def delete_item(self, item) -> None:
        """
        Удалить товар из корзины.

        :param item: Название товара

        :raise TypeError: Если товар не является строкой, вызывается ошибка
        :raise ValueError: Если товара нет в корзине, вызывается ошибка
        """
        if not isinstance(item, str):
            raise TypeError('item must be str')
        if item not in self._shop_cart:
            raise ValueError('there is no such item in the shop cart')
        self._shop_cart.remove(item)

    def greeting(self) -> str:
        """
        Возвращает приветствие.

        :return: Приветствие
        """
        return super().greeting() + ' покупателя!'

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта
        """
        return f"{super().__str__()}\nКорзина:{self._shop_cart}."

    def __repr__(self) -> str:
        """
        Возвращает представление объекта в виде строки, не выводит атрибут password, так как он не доступен для чтения.

        :return: Представление объекта в виде строки
        """
        return f"{super().__repr__()[:-1]}, shop_cart={self._shop_cart})"
