from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, isbn, title, subject, publisher, language, number_of_pages, book_format, pub_date):
        self.__isbn = isbn
        self.__title = title
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__number_of_pages = number_of_pages
        self.__book_format = book_format
        self.__pub_date = pub_date
        self.__authors = []
    
    def add_authors(self, author):
        self.__authors.append(author)