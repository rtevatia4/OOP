import datetime
from User import User

class Member(User):
    def __init__(self, id, password, person, card):
        super().__init__(id, password, person, card)
        self.__date_of_membership = datetime.date.today()
        self.__total_books_checked_out = 0
    
    def reset_password(self):
        pass

    def reserve_book_item(self, book_item):
        pass

    def increment_total_books_checked(self):
        self.__total_books_checked_out += 1
    
    def checkout_book_item(self, book_item):
        pass

    def return_book_item(self, book_item):
        pass

    def renew_book_item(self, book_item):
        pass
