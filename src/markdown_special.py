from src.special import Special


class MarkdownSpecial(Special):
    def __init__(self, item_name, markdown_amount, limit=False):
        super(MarkdownSpecial, self).__init__(item_name, limit=limit)
        self.markdown_amount = markdown_amount

    def calculate_discount_amount(self, items):
        num_discounted_units = self.calculate_number_of_discounted_units(items)
        return self.markdown_amount * num_discounted_units

    def calculate_number_of_discounted_units(self, items):
        total_units = sum([item.units for item in items])
        if self.limit:
            num_discounted_units = min(self.limit, total_units)
        else:
            num_discounted_units = total_units
        return num_discounted_units
