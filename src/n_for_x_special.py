from special import Special

class NforXSpecial(Special):
    def __init__(self, item_name, special_num, special_price, limit=False):
        super(NforXSpecial, self).__init__(item_name=item_name)
        self.special_num = special_num
        self.special_price = special_price
        self.limit = limit

    def calculate_discount_amount(self, items):
        if self.limit:
            items = items[:self.limit]
        item = items[0]
        total_units = sum([item.units for item in items])
        num_discounts = total_units // self.special_num
        actual_cost = item.price_per_unit * self.special_num
        return abs(actual_cost - self.special_price) * num_discounts
