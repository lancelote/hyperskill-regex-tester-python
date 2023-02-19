import pytest

from src.stage1.hw01 import PiggyBank


@pytest.mark.parametrize(
    "money_in,money_out",
    [((0, 99), (2, 0)), ((0, 88), (1, 89)), ((500, 500), (506, 1))],
)
def test_piggy_bank(money_in, money_out):
    piggy_bank = PiggyBank(1, 1)
    piggy_bank.add_money(*money_in)
    assert (piggy_bank.dollars, piggy_bank.cents) == money_out
