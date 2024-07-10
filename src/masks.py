def get_mask_card_number(card_2: str) -> str:
    """Функция, маскирующая номер карты"""
    return card_2.replace(card_2[6:-4], "******")


def get_mask_account(card_1: str) -> str:
    """ "Функция, маскирующая номер счета"""
    return card_1.replace(card_1[:-4], "**")
