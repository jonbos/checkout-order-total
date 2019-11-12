from itertools import groupby

from src.item import Item


class Transaction:
    def __init__(self, price_db=None, specials_db=None):
        if specials_db is None:
            specials_db = {}
        if price_db is None:
            price_db = {}

        self.items = []
        self.price_db = price_db
        self.specials_db = specials_db

    def scan(self, item_name, *args):
        item_price = self.price_db[item_name]
        if args:
            weight = args[0]
            item = Item(item_name, item_price, weight)
        else:
            item = Item(item_name, item_price)
        self.items.append(item)

    def add_special(self, special):
        item_name = special.item_name
        if item_name in self.specials_db:
            self.specials_db[item_name].append(special)
        else:
            self.specials_db[item_name] = [special]

    @property
    def total(self):
        item_total = self.get_pre_discount_transaction_total()
        discount_amount = self.calculate_transaction_discounts()
        return item_total - discount_amount

    def get_pre_discount_transaction_total(self):
        return sum([item.price_per_unit * item.units for item in self.items])

    def calculate_transaction_discounts(self):
        discount_amount = 0
        for item_name, items in groupby(self.items, lambda item: item.name):
            discount_amount += self.calculate_item_discounts(item_name, list(items))
        return discount_amount

    def calculate_item_discounts(self, item_name, item_list):
        discount_amount = 0
        item_discount_list = self.get_item_discounts(item_name)
        for discount in item_discount_list:
            discount_amount += discount.calculate_discount_amount(item_list)
        return discount_amount

    def get_item_discounts(self, item_name):
        return self.specials_db.get(item_name, [])
