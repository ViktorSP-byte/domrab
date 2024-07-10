import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("MasterCard7158300734726758", "MasterCard 715830******6758"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card(string: str, expected_result: str) -> None:
    assert mask_account_card(string) == expected_result


@pytest.fixture
def date() -> str:
    return "2018-07-11T02:26:18.671407"


def test_get_data(date: str) -> None:
    assert get_data(date) == "11.07.2018"
