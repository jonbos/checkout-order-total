from src.special import Special


class BulkSpecial(Special):
    def __init__(self, item_name, purchase_threshold, num_discounted, percent_discount, limit=False):
        super(BulkSpecial, self).__init__(item_name, limit)
        self.purchase_threshold = purchase_threshold
        self.num_discounted = num_discounted
        self.percent_discount = percent_discount

    def calculate_discount_amount(self, items):
        total_units = sum(item.units for item in items)
        item_price = items[0].price_per_unit

        if self.limit:
            total_units = min(total_units, self.limit)

        num_discounts = self.calculate_number_of_discounts(total_units)
        return self.calculate_discount_value(item_price) * num_discounts * self.num_discounted

    def calculate_number_of_discounts(self, num_units):
        return num_units // (self.purchase_threshold + self.num_discounted)

    def calculate_discount_value(self, item_price):
        return (item_price * (self.percent_discount / 100))
