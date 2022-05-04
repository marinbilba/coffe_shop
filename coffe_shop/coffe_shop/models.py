import enum
from abc import abstractmethod


class TeaTypes(enum.Enum):
    Green = 1
    Black = 2
    Mint = 3


class CoffeeTypes(enum.Enum):
    Espresso = 1
    Latte = 2
    Americano = 3


class JuiceType(enum.Enum):
    Apple = 1
    Orange = 2
    Carrot = 3


class DrinkSizes(enum.Enum):
    Small = 1
    Medium = 2
    Large = 3


class DrinkTypes(enum.Enum):
    Tea = 1
    Coffee = 2
    Juice = 3


class Product():
    def __init__(self, type, subtype, size):
        self.type = type
        self.subtype = subtype
        self.size = size

    @abstractmethod
    def get_price_without_vat(self):
        pass

    def get_price_with_vat(self):
        return self.get_price_without_vat() + self.get_price_without_vat() * 0.25


class Drink(Product):
    def __init__(self, drink_type, drink_subtype, drink_size):
        super().__init__(drink_type, drink_subtype, drink_size)
        self.type = drink_type.name
        self.sub_type = drink_subtype.name
        self.size = drink_size.name


    def to_string(self):
        print("type: " + self.type + '; sub_type: ' + self.sub_type + '; size: ' + self.size)

    def get_price_without_vat(self):
        initial_price = 0.0
        if self.type == 'Tea':
            if self.sub_type == 'Green':
                initial_price = 11.0
            elif self.sub_type == 'Black':
                initial_price = 12.0
            elif self.sub_type == 'Mint':
                initial_price = 13.0
        elif self.type == 'Coffee':
            if self.sub_type == 'Espresso':
                initial_price = 21.0
            elif self.sub_type == 'Latte':
                initial_price = 22.0
            elif self.sub_type == 'Americano':
                initial_price = 23.0
        elif self.type == 'Juice':
            if self.sub_type == 'Apple':
                initial_price = 31.0
            elif self.sub_type == 'Orange':
                initial_price = 32.0
            elif self.sub_type == 'Carrot':
                initial_price = 33.0

        if self.size == 'Small':
            return initial_price
        elif self.size == 'Medium':
            return initial_price + initial_price * 0.25
        elif self.size == 'Large':
            return initial_price + initial_price * 0.50
