# A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
# B. Abstractions should not depend on details. Details should depend upon abstractions.
class Exchange:
    def get_orderbook(self):
        pass

class StockPrices:
    def __init__(self, exchange: Exchange):
        self.exchange = exchange
    
    def determine_price(self):
        data = self.exchange.get_orderbook()
        # calculate price
        print("Pricedata:", data)

# In above example StockPrice class depends on Exchange class and its concrete implementation
# Both classes are tightly coupled

# Below is following the dependency inversion
from abc import ABC, abstractmethod
class DataSource:
    @abstractmethod
    def get_orderbook(self):
        pass

class ExchangeA(DataSource):
    def get_orderbook(self):
        pass

class ExchangeB(DataSource):
    def get_orderbook(self):
        pass

class StockPrices:
    def __init__(self, datasource: DataSource):
        self.datasource = datasource
    
    def determine_price(self):
        data = self.datasource.get_orderbook()
        # calculate price
        print("Pricedata:", data)

