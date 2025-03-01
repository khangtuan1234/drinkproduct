from abc import ABC, abstractmethod
 
class product(ABC):
    @abstractmethod
    def getName(self):
        pass
   
    @abstractmethod
    def getPrice(self):
        pass
 
class tra(product):
    def __init__(self, name, price):
        self.name = name
        self.base_price = price
        self.size = 'S'  
   
    def setSize(self, size):
        self.size = size
   
    def getPrice(self):
        size_charge = {'S': 0, 'M': 5, 'L': 10}
        return self.base_price + size_charge.get(self.size, 0)
   
    def getName(self):
        return self.name
 
class cafe(product):
    def __init__(self, name, price):
        self.name = name
        self.base_price = price
        self.size = 'S'  
   
    def setSize(self, size):
        self.size = size
   
    def getPrice(self):
        size_charge = {'S': 0, 'M': 5, 'L': 10}
        return self.base_price + size_charge.get(self.size, 0)
   
    def getName(self):
        return self.name
 
class bakery(product):
    def __init__(self, name, price):
        self.name = name
        self.price = price
   
    def getPrice(self):
        return self.price
   
    def getName(self):
        return self.name
travai = tra('tra vai', 40)
travai.setSize('L')
print(travai.getName(), 'costs', travai.getPrice())