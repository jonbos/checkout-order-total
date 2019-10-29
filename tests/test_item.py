import pytest

from src.item import ByEachItem, ByWeightItem


class TestByEachItem:
    def test_should_create_item_with_name_and_price(self):
        milk = ByEachItem('gallon of milk', 3.98)

        assert milk.name == 'gallon of milk'
        assert milk.price_per_unit == 3.98

    def test_items_are_equal_when_they_have_the_same_name_and_price(self):
        milk = ByEachItem('gallon of milk', 3.98)
        other_milk = ByEachItem('gallon of milk', 3.98)
        heavy_cream = ByEachItem('quart of heavy cream', 5.99)

        assert milk == other_milk
        assert milk != heavy_cream


class TestByWeightItem:
    def test_by_weight_items_have_qty(self):
        bulk_chocolate = ByWeightItem('bulk chocolate', 7.99, 3)
        assert bulk_chocolate.qty == 3

    def test_by_weight_items_price_calculation(self):
        olive_oil = ByWeightItem('olive oil', 2.99, 10)
        assert pytest.approx(olive_oil.price, 29.99)
