
class BookLending:
    def __init__(self, creation_date, due_date, book_item_id, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__book_item_id = book_item_id
        self.__member_id = member_id
        self.__return_date = None
        self.__book_reservation = None
        self.__user = None
    
    def lend_book(self):
        pass

    def fetch_lending_details(self, item_id):
        pass