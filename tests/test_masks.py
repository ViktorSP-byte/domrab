import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("7158300734726758", "715830******6758"),
        ("7158300734726759", "715830******6759"),
    ],
)
def test_get_mask_card_number(string: str, expected_result: str) -> None:
    assert get_mask_card_number(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("12345678901234567340", "**7340"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(string: str, expected_result: str) -> None:
    assert get_mask_account(string) == expected_result
