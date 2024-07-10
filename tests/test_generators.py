from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_data) -> None:
    usd_transactions = filter_by_currency(transactions_data, "USD")
    assert next(usd_transactions) == {'id': 939719570,
                               'state': 'EXECUTED',
                               'date': '2018-06-30T02:08:58.425572',
                               'operationAmount':
                                   {'amount': '9824.07',
                                    'currency': {
                                           'name': 'USD',
                                           'code': 'USD'
                                         }
                                    },
                               'description': 'Перевод организации',
                               'from': 'Счет 75106830613657916952',
                               'to': 'Счет 11776614605963066702'}
    assert next(usd_transactions) == {'id': 142264268,
                               'state': 'EXECUTED',
                               'date': '2019-04-04T23:20:05.206878',
                               'operationAmount':
                                   {'amount': '79114.93',
                                    'currency': {
                                            'name': 'USD',
                                            'code': 'USD'
                                         }
                                    },
                               'description': 'Перевод со счета на счет',
                               'from': 'Счет 19708645243227258542',
                               'to': 'Счет 75651667383060284188'}
    rub_transactions = filter_by_currency(transactions_data, "RUB")
    assert next(rub_transactions) == {"id": 873106923,
                                      "state": "EXECUTED",
                                      "date": "2019-03-23T01:09:46.296404",
                                      "operationAmount": {
                                              "amount": "43318.34",
                                              "currency": {
                                                  "name": "руб.",
                                                  "code": "RUB"
                                              }
                                      },
                                      "description": "Перевод со счета на счет",
                                      "from": "Счет 44812258784861134719",
                                      "to": "Счет 74489636417521191160"
                                      }

    assert next(rub_transactions) == {"id": 594226727,
                                      "state": "CANCELED",
                                      "date": "2018-09-12T21:27:25.241689",
                                      "operationAmount": {
                                          "amount": "67314.70",
                                          "currency": {
                                              "name": "руб.",
                                              "code": "RUB"
                                          }
                                      },
                                      "description": "Перевод организации",
                                      "from": "Visa Platinum 1246377376343588",
                                      "to": "Счет 14211924144426031657"
                                      }


def test_filter_by_currency_empty_currency(transactions_data) -> None:
    assert list(filter_by_currency(transactions_data, "")) == []


def test_filter_by_currency_not_existed_currency(transactions_data) -> None:
    assert list(filter_by_currency(transactions_data, "ERI")) == []


def test_transaction_description(transactions_data):
    expected_result = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    trans = transaction_descriptions(transactions_data)
    assert list(trans) == expected_result


def test_card_number_generator():
    num = card_number_generator(x=1, y=5)
    assert next(num) == "0000 0000 0000 0001"
    assert next(num) == "0000 0000 0000 0002"
    assert next(num) == "0000 0000 0000 0003"
    assert next(num) == "0000 0000 0000 0004"
    assert next(num) == "0000 0000 0000 0005"
