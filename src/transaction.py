from itertools import groupby

from src.item import Item


class Transaction:
    def __init__(self, price_db=None, markdown_db=None, bulk_db=None):
        if markdown_db is None:
            markdown_db = {}
        if price_db is None:
            price_db = {}
        if bulk_db is None:
            bulk_db = {}

        self.items = []
        self.price_db = price_db
        self.markdown_db = markdown_db
        self.bulk_db = bulk_db

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
            total += item.price - self.get_markdown_amount(item)
        bulk_discount = self.calculate_bulk_discount_amount(self.items)
        return total - bulk_discount

    def get_markdown_amount(self, item):
        if item.name in self.markdown_db:
            return self.markdown_db[item.name].markdown_amount * item.units
        else:
            return 0

    def calculate_bulk_discount_amount(self, items):
        discount_amount = 0
        for item_name, list_items in groupby(items, lambda x: x.name):
            if item_name in self.bulk_db:
                list_items = list(list_items)
                discount_amount += list_items[0].price * .50 * len(list_items)
        return discount_amount
