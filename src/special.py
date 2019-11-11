class Special:
    def __init__(self, item_name, limit=None):
        self.item_name = item_name
        self.limit = limit

    @staticmethod
    def calculate_discount_amount(self, items):
        raise NotImplementedError
