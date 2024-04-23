from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, status, timestamp):
        self.__amount = amount
        self.__status = status
        self.__timestamp = timestamp
    
    @abstractmethod
    def initiate_payment(self):
        pass

class Cash(Payment):
    def __init__(self, amount, status, timestamp):
        super().__init__(amount, status, timestamp)
    
    def initiate_payment(self):
        pass

class CreditCard(Payment):
    def __init__(self, amount, status, timestamp):
        super().__init__(amount, status, timestamp)
    
    def initiate_payment(self):
        pass