import pytest

from src.transaction import Transaction


@pytest.fixture
def get_test_db():
    return {"14oz soup": 1.89, '80% ground beef': 5.99, 'Bananas': 2.38}

def test_a_new_transaction_has_zero_total():
    trans = Transaction()
    assert trans.total == 0


def test_a_new_transaction_has_zero_items():
    trans = Transaction()
    assert len(trans.items) == 0


def test_a_transaction_has_a_price_db():
    trans = Transaction()
    assert trans.price_db is not None


def test_can_instantiate_with_price_db(get_test_db):
    trans = Transaction(get_test_db)
    assert trans.price_db == get_test_db
