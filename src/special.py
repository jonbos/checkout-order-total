class Special:
    def __init__(self, item_name, limit):
        self.item_name = item_name
        self.limit = limit

    def calculate_discount_amount(self, items):
        raise NotImplementedError
