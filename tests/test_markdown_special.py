import pytest

from src.markdown_special import MarkdownSpecial
from src.transaction import Transaction
# noinspection PyUnresolvedReferences
from .test_transaction import get_test_db


class TestMarkdownPricing:
    @pytest.fixture
    def get_markdown_special_db(self):
        return {'14oz soup': [MarkdownSpecial('14oz soup', .2)],
                '80% ground beef': [MarkdownSpecial('80% ground beef', .50)]}

    def test_should_reduce_cost_by_markdown_amount(self, get_test_db, get_markdown_special_db):
        trans = Transaction(price_db=get_test_db, specials_db=get_markdown_special_db)

        trans.scan('14oz soup')

        assert trans.total == 1.69

    def test_should_reduce_cost_by_markdown_amount_for_by_weight_items(self, get_test_db, get_markdown_special_db):
        trans = Transaction(get_test_db, get_markdown_special_db)
        print(get_markdown_special_db)
        trans.scan('80% ground beef', 2)

        assert trans.total == 10.98
