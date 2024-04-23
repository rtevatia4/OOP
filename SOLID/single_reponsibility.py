# Class voilating single responsibility 
# Here we have multiple responsilities in a class and it has many reasons to change the implmentation
class Orders:
    def __init__(self, name, amount):
        self._name = name
        self._amount = amount
    
    def get_name(self):
        return self._name

    def get_amount(self):
        return self._amount
    
    def generate_receipt(self):
        pass

    def save_to_DB(self):
        pass

# Below implementation follow Single Responsility
class Orders:
    def __init__(self, name, amount):
        self._name = name
        self._amount = amount
    
    def get_name(self):
        return self._name

class Receipt:
    def get_order_details(self) -> Orders:
        pass

    def generate_receipt(self, order: Orders):
        pass

class OrdersDB:
    def get_order_details(self) -> Orders:
        pass

    def save_to_db(self, order: Orders):
        pass
