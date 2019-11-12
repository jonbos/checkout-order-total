from src.special import Special


class BulkSpecial(Special):
    def __init__(self, item_name, purchase_amount, discount_amount, percent_discount, limit=False):
        super(BulkSpecial, self).__init__(item_name)
        self.purchase_amount = purchase_amount
        self.discount_amount = discount_amount
        self.percent_discount = percent_discount

    def calculate_discount_amount(self, items):
        if self.limit:
            items = items[:self.limit]

        num_units = sum(item.units for item in items)
        num_discounts = num_units // (self.purchase_amount + self.discount_amount)
        item_price = items[0].price_per_unit
        return (item_price * self.percent_discount / 100) * num_discounts * self.discount_amount
