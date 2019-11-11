from src.bulk_special import BulkSpecial
from src.item import Item

one_dollar_item = Item('one dollar item', 1)
two_pounds_of_one_dollar_item = Item('one dollar item', 1, 2)

bogo_one_dollar_item = BulkSpecial('one_dollar_item', 1, 1, 100)
buy_two_get_one_half_off_one_dollar_item = BulkSpecial('one_dollar_item', 2, 1, 50)
buy_two_get_two_free_one_dollar_item = BulkSpecial('one dollar item', 2, 2, 100)


def test_should_return_correct_total_for_buy_one_get_one_free_if_buying_two_items():
    items = [one_dollar_item] * 2
    discount_amt = bogo_one_dollar_item.calculate_discount_amount(items)
    assert discount_amt == 1


def test_should_return_proper_price_on_BOGO_on_by_weight_item():
    items = [two_pounds_of_one_dollar_item, two_pounds_of_one_dollar_item]
    discount_amt = buy_two_get_two_free_one_dollar_item.calculate_discount_amount(items)
    assert discount_amt == 2


def test_buying_three_items_only_nets_one_free_when_BOGO():
    items = [one_dollar_item] * 3
    discount_amount = bogo_one_dollar_item.calculate_discount_amount(items)
    assert discount_amount == 1


def test_buying_six_items_discounts_3_when_BOGO():
    items = [one_dollar_item] * 6
    discount_amount = bogo_one_dollar_item.calculate_discount_amount(items)
    assert discount_amount == 3


def test_buy_two_get_one_half_off():
    items = [one_dollar_item] * 3
    discount_amount = buy_two_get_one_half_off_one_dollar_item.calculate_discount_amount(items)
    assert discount_amount == .5
