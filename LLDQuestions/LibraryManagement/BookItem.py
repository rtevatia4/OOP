from Book import Book
class BookItem(Book):
    def __init__(self, id, is_reference_only, borrowed, due_date, price, status, date_of_purchase, publication_date, placed_at):
        super().__init__(None, None, None, None, None, 0, None, None)  # Calling the parent class constructor
        self.id = id
        self.is_reference_only = is_reference_only
        self.borrowed = borrowed
        self.due_date = due_date
        self.price = price
        self.status = status
        self.date_of_purchase = date_of_purchase
        self.publication_date = publication_date
        self.placed_at = placed_at
        self.book = None  # Composition: BookItem has a reference to a Book
    
    def checkout(self, member_id):
        # checkout logic, update status, set due date etc.
        return True

    def set_placed_at(self, rack):
        self.placed_at = rack
    
    def set_added_by(self, librarian):
        pass

    def get_book(self):
        return self.book
