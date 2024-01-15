from typing import Optional, List


class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):
            raise TypeError("id must be integer")
        self.id = id
        if not isinstance(name, str):
            raise TypeError("name must be string")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError("pages must be integer")
        self.pages = pages

    def __str__(self):
        return f'Книга \"{self.name}\"'

    def __repr__(self):
        return f'Book(id={self.id}, name=\'{self.name}\', pages={self.pages})'


class Library:
    def __init__(self, books: Optional[List[Book]] = None):
        if books is None:
            books = []
        elif not isinstance(books, list) or not all(isinstance(book, Book) for book in books):
            raise TypeError("books must be list of Book")
        self.books = books

    def get_next_book_id(self):
        length = len(self.books)
        if length:
            return self.books[length - 1].id + 1
        else:
            return 1

    def get_index_by_book_id(self, id):
        if not isinstance(id, int):
            raise TypeError("id must be integer")
        for index, item in enumerate(self.books):
            if item.id == id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
