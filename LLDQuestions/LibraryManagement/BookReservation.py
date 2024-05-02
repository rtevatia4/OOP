
class BookReservation:
    def __init__(self, creation_data, status, item_id, member_id):
        self.__creation_date = creation_data
        self.__status = status
        self.__item_id = item_id
        self.__member_id = member_id
    
    def fetch_reservation_details(self, book_item_id):
        pass
