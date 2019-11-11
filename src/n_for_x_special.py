from special import Special


class NforXSpecial(Special):
    def __init__(self, item_name, special_num, special_price):
        super(NforXSpecial, self).__init__(item_name=item_name)
        self.special_num = special_num
        self.special_price = special_price

    def calculate_discount_amount(self, items):
        item = items[0]
        actual_cost = item.price_per_unit * self.special_num
        return abs(actual_cost - self.special_price)
