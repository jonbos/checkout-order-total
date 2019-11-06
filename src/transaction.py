from src.item import Item

class Transaction:
    def __init__(self, price_db=None, markdown_db=None):
        if markdown_db is None:
            markdown_db = {}
        if price_db is None:
            price_db = {}

        self.items = []
        self.price_db = price_db
        self.markdown_db = markdown_db

    def scan(self, item_name, *args):
        item_price = self.price_db[item_name]
        if args:
            weight = args[0]
            item = Item(item_name, item_price, weight)
        else:
            item = Item(item_name, item_price)
        self.items.append(item)

    @property
    def total(self):
        total = 0
        for item in self.items:
            total += item.price - ((self.markdown_db.get(item.name, 0) * item.units))
        return total
