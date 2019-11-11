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

    @property
    def total(self):
        item_total = sum([item.price_per_unit * item.units for item in self.items])
        discount_amount = self.calculate_discounts()
        return item_total - discount_amount

    def calculate_discounts(self):
        discount_amount = 0
        for item_name, list_items in groupby(self.items, lambda item: item.name):
            if item_name in self.specials_db:
                for discount in self.specials_db[item_name]:
                    discount_amount += discount.calculate_discount_amount(list(list_items))

        return discount_amount

    def calculate_bulk_discount_amount(self, items):
        discount_amount = 0
        for item_name, list_items in groupby(items, lambda x: x.name):
            if item_name in self.bulk_db:
                list_items = list(list_items)
                discount_amount += list_items[0].price * .50 * len(list_items)
        return discount_amount
