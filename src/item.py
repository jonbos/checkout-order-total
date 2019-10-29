class Item:
    def __init__(self, name, price_per_unit):
        self.name = name
        self.price_per_unit = price_per_unit

    @property
    def price(self):
        return self.price_per_unit

    def __eq__(self, other):
        return self.price_per_unit == other.price_per_unit and self.name == other.name


class ByEachItem(Item):
    def __init__(self, name, price_per_unit):
        super(ByEachItem, self).__init__(name, price_per_unit)


class ByWeightItem(Item):
    def __init__(self, name, price_per_unit, qty):
        super(ByWeightItem, self).__init__(name, price_per_unit)
        self.qty = qty

    @property
    def price(self):
        return self.price_per_unit * self.qty
