class Item:
    def __init__(self, name, price_per_unit, units=1):
        self.name = name
        self.price_per_unit = price_per_unit
        self.units = units

    @property
    def price(self):
        return self.price_per_unit * self.units

    def __eq__(self, other):
        return self.price_per_unit == other.price_per_unit and self.name == other.name
