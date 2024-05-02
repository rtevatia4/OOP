from User import User
class Librarian(User):
    def __init__(self, id, password, person, card):
        super().__init(id,password,person, card)
    
    def reset_password(self):
        pass
    
    def add_book_item(self, book_item):
        pass

    def block_member(self, member):
        pass

    def unblock_member(self, member):
        pass

