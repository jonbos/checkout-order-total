class Transaction:
    def __init__(self, price_db=None):
        if price_db is None:
            price_db = {}
        self.total = 0
        self.items = []
        self.price_db = dict(price_db)
