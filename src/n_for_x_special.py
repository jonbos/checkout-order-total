from special import Special

class NforXSpecial(Special):
    def __init__(self, item_name, num_of_items, price, limit=False):
        super(NforXSpecial, self).__init__(item_name=item_name, limit=limit)
        self.num_of_items = num_of_items
        self.price = price

    def calculate_discount_amount(self, items):
        item = items[0]
        num_discounted_units = self.calculate_num_discounted_units(items)
        num_discounts = num_discounted_units // self.num_of_items
        discount_value = self.calculate_discount_value(item)
        return discount_value * num_discounts

    def calculate_discount_value(self, item):
        item_price = item.price_per_unit
        actual_price = self.num_of_items * item_price
        discount_price = self.price

        return abs(actual_price - discount_price)

    def calculate_num_discounted_units(self, items):
        total_units = sum([item.units for item in items])
        if self.limit:
            return min(self.limit, total_units)
        else:
            return total_units
