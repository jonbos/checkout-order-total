from src.special import Special


class MarkdownSpecial(Special):
    def __init__(self, item_name, markdown_amount, limit=False):
        super(MarkdownSpecial, self).__init__(item_name)
        self.markdown_amount = markdown_amount
        self.limit = limit

    def calculate_discount_amount(self, items):
        if self.limit:
            items = items[:self.limit]
        num_units = sum([item.units for item in items])
        return self.markdown_amount * num_units
