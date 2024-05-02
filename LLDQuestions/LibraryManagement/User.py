from abc import ABC, abstractmethod
from Enums import AccountStatus

class User(ABC):
    def __init__(self, id, password, person, card):
        self.__id = id
        self.__password = password
        self.__status = AccountStatus.ACTIVE
        self.__person = person
        self.__card = card
    
    @abstractmethod
    def reset_password(self):
        pass

