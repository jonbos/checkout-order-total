import pytest

from src.item import Item


class TestByEachItem:
    def test_should_create_item_with_name_and_price(self):
        milk = Item('gallon of milk', 3.98)

        assert milk.name == 'gallon of milk'
        assert milk.price_per_unit == 3.98

    def test_items_are_equal_when_they_have_the_same_name_and_price(self):
        milk = Item('gallon of milk', 3.98)
        other_milk = Item('gallon of milk', 3.98)
        heavy_cream = Item('quart of heavy cream', 5.99)

        assert milk == other_milk
        assert milk != heavy_cream


class TestByWeightItem:
    def test_items_can_have_units(self):
        bulk_chocolate = Item('bulk chocolate', 7.99, 3)
        assert bulk_chocolate.units == 3

    def test_by_weight_items_price_calculation(self):
        olive_oil = Item('olive oil', 2.99, 10)
        assert pytest.approx(olive_oil.price, 29.99)
