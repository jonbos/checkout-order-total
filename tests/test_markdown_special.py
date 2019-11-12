import pytest

from item import Item
from src.markdown_special import MarkdownSpecial


@pytest.fixture
def get_item_list_with_single_one_dollar_item():
    return [Item('one dollar item', 1)]


@pytest.fixture
def get_item_list_with_two_units_single_one_dollar_item():
    return [Item('one dollar item', 1, 2)]


class TestUnlimitedMarkdownPricing:

    def test_should_calculate_price_less_markdown_for_single_item(self, get_item_list_with_single_one_dollar_item):
        items = get_item_list_with_single_one_dollar_item
        ten_percent_markdown = MarkdownSpecial('one dollar item', .1)

        discount_amt = ten_percent_markdown.calculate_discount_amount(items)

        assert discount_amt == .1

    def test_should_calculate_markdown_cost_for_multiple_items(self, get_item_list_with_single_one_dollar_item):
        items = get_item_list_with_single_one_dollar_item * 5
        ten_percent_markdown = MarkdownSpecial('one dollar item', .1)

        discount_amt = ten_percent_markdown.calculate_discount_amount(items)

        assert discount_amt == .5

    def test_should_calculate_markdown_amount_for_multiple_by_weight_items(self,
                                                                           get_item_list_with_two_units_single_one_dollar_item):
        items = get_item_list_with_two_units_single_one_dollar_item * 2
        ten_percent_markdown = MarkdownSpecial('one dollar per pound item', .1)

        discount_amt = ten_percent_markdown.calculate_discount_amount(items)

        assert discount_amt == .4

    def test_should_calculate_markdown_amount_for_single_by_weight_items(self,
                                                                         get_item_list_with_two_units_single_one_dollar_item):
        items = get_item_list_with_two_units_single_one_dollar_item
        ten_percent_markdown = MarkdownSpecial('one dollar per pound item', .1)

        discount_amt = ten_percent_markdown.calculate_discount_amount(items)

        assert discount_amt == .2


class TestMarkdownWithLimit:
    @pytest.fixture
    def get_ten_cent_markdown_limit_2(self):
        return MarkdownSpecial('one dollar item', .1, 2)

    def test_should_calculate_discount_amount_when_num_of_items_equals_limit(self,
                                                                             get_item_list_with_single_one_dollar_item,
                                                                             get_ten_cent_markdown_limit_2):
        items = get_item_list_with_single_one_dollar_item * 2
        markdown = get_ten_cent_markdown_limit_2

        discount_amt = markdown.calculate_discount_amount(items)

        assert discount_amt == .2

    def test_should_calculate_discount_amount_when_num_of_items_exceeds_limit(self,
                                                                              get_item_list_with_single_one_dollar_item,
                                                                              get_ten_cent_markdown_limit_2):
        items = get_item_list_with_single_one_dollar_item * 3
        markdown = get_ten_cent_markdown_limit_2

        discount_amt = markdown.calculate_discount_amount(items)

        assert discount_amt == .2

    def test_should_calculate_discount_amount_when_num_of_items_exceeds_limit_weighted_items(self,
                                                                                             get_item_list_with_two_units_single_one_dollar_item,
                                                                                             get_ten_cent_markdown_limit_2):
        items = get_item_list_with_two_units_single_one_dollar_item * 2
        markdown = get_ten_cent_markdown_limit_2

        discount_amt = markdown.calculate_discount_amount(items)

        assert discount_amt == .2
