import pandas as pd
from unittest.mock import patch, mock_open
from src.csv_pandas import read_csv, read_pd  # Замените на имя вашего модуля


def test_read_csv():
    mock_file = "date;amount;description\n2025-01-01;100;Payment\n2025-02-01;200;Deposit\n"
    with patch("builtins.open", mock_open(read_data=mock_file)):
        result = read_csv("mock.csv")
        expected = [{"date": "2025-01-01", "amount": "100", "description": "Payment"},
                    {"date": "2025-02-01", "amount": "200", "description": "Deposit"}]
        assert result == expected


def test_read_pd():
    mock_df = pd.DataFrame({"date": ["2025-01-01", "2025-02-01"],
                            "amount": [100, 200],
                            "description": ["Payment", "Deposit"]})

    with patch("pandas.read_excel", return_value=mock_df):
        result = read_pd("mock.xlsx")
        expected = {"date": ["2025-01-01", "2025-02-01"],
                    "amount": [100, 200],
                    "description": ["Payment", "Deposit"]}
        assert result == expected
