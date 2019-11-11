class Markdown:
    def __init__(self, item_name, markdown_amount):
        self.item_name = item_name
        self.markdown_amount = markdown_amount

    def calculate_discount_amount(self, items):
        num_units = sum([item.units for item in items])
        return self.markdown_amount * num_units
