from src.widget import get_date, mask_account_card
import pytest


@pytest.mark.parametrize('card_or_account, masck_card_account',
                         [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                          ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(card_or_account, masck_card_account):
    assert mask_account_card(card_or_account) == masck_card_account


@pytest.mark.parametrize('input_time, output_time', [("2024-03-11T02:26:18.671407", "11:03:2024")])
def test_get_date(input_time, output_time):
    assert get_date(input_time) == output_time
