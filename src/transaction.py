from src.item import ByEachItem, ByWeightItem

class Transaction:
    def __init__(self, price_db=None):
        if price_db is None:
            price_db = {}
        self.items = []
        self.price_db = dict(price_db)

    def scan(self, item_name, *args):
        item_price = self.price_db[item_name]
        if args:
            weight = args[0]
            item = ByWeightItem(item_name, item_price, weight)
        else:
            item = ByEachItem(item_name, item_price)
        self.items.append(item)

    @property
    def total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
