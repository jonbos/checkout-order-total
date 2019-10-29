from src.transaction import Transaction


def test_a_new_transaction_has_zero_total():
    trans = Transaction()
    assert trans.total == 0
