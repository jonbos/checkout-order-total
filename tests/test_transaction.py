import pytest

from src.item import Item
from src.markdown_special import MarkdownSpecial
from src.transaction import Transaction


@pytest.fixture
def get_test_db():
    return {"14oz soup": 1.89, '80% ground beef': 5.99, 'Bananas': 2.38, 't-bone steak': 9.99}

@pytest.fixture
def get_transaction_with_test_db(get_test_db):
    return Transaction(get_test_db)

class TestWiring:
    def test_a_new_transaction_has_zero_total(self):
        trans = Transaction()
        assert trans.total == 0

    def test_a_new_transaction_has_zero_items(self):
        trans = Transaction()
        assert len(trans.items) == 0

    def test_a_transaction_has_a_price_db(self):
        trans = Transaction()
        assert trans.price_db is not None

    def test_can_instantiate_with_price_db(self, get_test_db):
        trans = Transaction(get_test_db)
        assert trans.price_db == get_test_db

    def test_can_add_special_to_transaction(self, get_test_db):
        special = MarkdownSpecial('14oz soup', 1.69)
        trans = Transaction(get_test_db)
        trans.add_special(special)
        assert trans.specials_db == {'14oz soup': [special]}

class TestScanningIndividualItems:
    def test_can_scan_item(self, get_test_db):
        trans = Transaction(get_test_db)
        expected = Item('14oz soup', 1.89)

        trans.scan('14oz soup')

        assert trans.items[0] == expected

    def test_scanning_an_item_increases_transaction_total(self, get_transaction_with_test_db):
        trans = get_transaction_with_test_db

        trans.scan("14oz soup")

        assert trans.total == 1.89

    def test_adding_multiple_items_increases_cost_with_each_item(self, get_test_db, get_transaction_with_test_db):
        price_db = get_test_db
        trans = get_transaction_with_test_db

        trans.scan('14oz soup')
        assert trans.total == price_db['14oz soup']
        trans.scan('t-bone steak')
        assert trans.total == price_db['14oz soup'] + price_db['t-bone steak']


class TestByWeightItemScanning:
    def test_can_scan_item_with_weight(self, get_transaction_with_test_db, get_test_db):
        trans = get_transaction_with_test_db

        trans.scan('80% ground beef', 2.5)

        assert pytest.approx(trans.total, get_test_db['80% ground beef'] * 2.5)



