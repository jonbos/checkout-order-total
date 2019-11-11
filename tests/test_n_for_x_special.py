from src.item import Item
from src.n_for_x_special import NforXSpecial

one_dollar_item = Item('one dollar item', 1)
two_pounds_of_one_dollar_item = Item('one dollar item', 1, 2)


def test_5_for_4_special_pricing():
    items = [one_dollar_item] * 5
    five_for_four = NforXSpecial('one_dollar_item', 5, 4)
    discount_amount = five_for_four.calculate_discount_amount(items)
    assert discount_amount == 1


def test_4_for_3_weighted_item():
    items = [two_pounds_of_one_dollar_item] * 2
    four_for_three = NforXSpecial('one_dollar_item', 4, 3)
    discount_amount = four_for_three.calculate_discount_amount(items)
    assert discount_amount == 1
