from src.mascks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
import pytest


@pytest.fixture
def error_number_card():
    return "Неккоректный номер карты"


@pytest.mark.parametrize('num_card, masck_all, masck_four', [(7000793594646361, "7000 79** **** 6361", "**6361"),
                                                             (6384625346374824, "6384 62** **** 4824", "**4824")])


def test_input_get_mask_card_number(error_number_card):
    assert get_mask_card_number(234) == error_number_card
    assert get_mask_card_number("dдллдлвлtjjdjdgjddgоhf") == error_number_card


def test_input_get_mask_account(error_number_card):
    assert get_mask_account(234) == error_number_card
    assert get_mask_account("dдллдлвлtjjdjdgjddgоhf") == error_number_card


def test_get_mask_card_number(num_card, masck_all, masck_four):
    assert get_mask_card_number(num_card) == masck_all
    assert get_mask_account(num_card) == masck_four


@pytest.mark.parametrize('input_state, output_state', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                         [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])


def test_filter_by_state(input_state, output_state):
    assert filter_by_state(input_state) == output_state


@pytest.mark.parametrize('input_date, output_date',
                         [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                         [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])


def test_filter_by_date(input_date, output_date):
    assert filter_by_state(input_date) == output_date


@pytest.mark.parametrize('card_or_account, masck_card_account',
                         [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                          ("Счет 73654108430135874305", "Счет **4305")])


def test_mask_account_card(card_or_account, masck_card_account):
    assert mask_account_card(card_or_account) == masck_card_account


@pytest.mark.parametrize('input_time, output_time', [("2024-03-11T02:26:18.671407", "11:03:2024")])


def test_mask_account_card(input_time, output_time):
    assert mask_account_card(input_time) == output_time
