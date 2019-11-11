from src.special import Special


class BulkSpecial(Special):
    def __init__(self, item_name, purchase_amount, discount_amount, percent_discount):
        super(BulkSpecial, self).__init__(item_name)
        self.purchase_amount = purchase_amount
        self.discount_amount = discount_amount
        self.percent_discount = percent_discount

    def calculate_discount_amount(self, items):
        num_units = sum(item.units for item in items)
        if num_units >= self.purchase_amount + self.discount_amount:
            return items[0].price_per_unit
