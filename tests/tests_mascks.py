from src.mascks import get_mask_card_number, get_mask_account
import pytest


@pytest.fixture
def error_number_card():
    return "Неккоректный номер карты"


def test_input_get_mask_card_number(error_number_card):
    assert get_mask_card_number(234) == error_number_card
    assert get_mask_card_number("dдллдлвлtjjdjdgjddgоhf") == error_number_card


def test_input_get_mask_account(error_number_card):
    assert get_mask_account(234) == error_number_card
    assert get_mask_account("dдллдлвлtjjdjdgjddgоhf") == error_number_card


def test_get_mask_card_number():
    assert get_mask_card_number(7000793594646361) == "7000 79** **** 6361"
    assert get_mask_account(7000793594646361) == "**6361"
