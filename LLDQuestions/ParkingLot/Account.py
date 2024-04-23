from abc import ABC, abstractmethod

class Account(ABC):
  # Data members
    def __init__(self, user_name, password, person, status):
        self.__user_name = user_name
        self.__password = password
        self.__person = person # Refers to an instance of the Person class
        self.__status = status # Refers to the AccountStatus enum

    @abstractmethod
    def reset_password(self):
        pass

class Admin(Account):
    def __init__(self, user_name, password, person, status):
        super().__init__(user_name, password, person, status)
    
    def add_parking_spot(self, spot):
        pass

    def add_display_board(self, diaply_board):
        pass

    def add_entrance(self, entrance):
        pass

    def add_exit(self, exit):
        pass

    def reset_password(self):
        pass

class ParkingAttendent(Account):
    def __init__(self, user_name, password, person, status):
        super().__init__(user_name, password, person, status)
    
    def process_ticket(self, parking_ticket):
        pass

    def reset_password(self):
        pass



