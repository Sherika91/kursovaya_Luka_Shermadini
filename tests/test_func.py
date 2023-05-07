from utils import func
from utils.data_for_widget import load_bank_data
import os.path


all_data = os.path.join('../operations.json')

data = [{
      "id": 147815167,
      "state": "EXECUTED",
      "date": "2018-01-26T15:40:13.413061",
      "operationAmount": {
        "amount": "50870.71",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Перевод с карты на счет",
      "from": "Maestro 4598300720424501",
      "to": "Счет 43597928997568165086"
    },
    {
      "id": 518707726,
      "state": "EXECUTED",
      "date": "2018-11-29T07:18:23.941293",
      "operationAmount": {
        "amount": "3348.98",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод с карты на карту",
      "from": "MasterCard 3152479541115065",
      "to": "Visa Gold 9447344650495960"
    },
    {
      "id": 649467725,
      "state": "EXECUTED",
      "date": "2018-04-14T19:35:28.978265",
      "operationAmount": {
        "amount": "96995.73",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Перевод организации",
      "from": "Счет 27248529432547658655",
      "to": "Счет 97584898735659638967"
    },
    {
      "id": 782295999,
      "state": "EXECUTED",
      "date": "2019-09-11T17:30:34.445824",
      "operationAmount": {
        "amount": "54280.01",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "Счет 24763316288121894080",
      "to": "Счет 96291777776753236930"
    },
    {
      "id": 542678139,
      "state": "EXECUTED",
      "date": "2018-10-14T22:27:25.205631",
      "operationAmount": {
        "amount": "90582.51",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "Visa Platinum 2256483756542539",
      "to": "Счет 78808375133947439319"
    },
    {
      "id": 558167602,
      "state": "EXECUTED",
      "date": "2019-04-12T17:27:27.896421",
      "operationAmount": {
        "amount": "43861.89",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод со счета на счет",
      "from": "Счет 73654108430135874305",
      "to": "Счет 89685546118890842412"
    },
    ]


def test_sorted_data():
    list_sorted = [{'id': 782295999, 'state': 'EXECUTED', 'date': '2019-09-11T17:30:34.445824', 'operationAmount': {'amount': '54280.01', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 24763316288121894080', 'to': 'Счет 96291777776753236930'}, {'id': 558167602, 'state': 'EXECUTED', 'date': '2019-04-12T17:27:27.896421', 'operationAmount': {'amount': '43861.89', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 73654108430135874305', 'to': 'Счет 89685546118890842412'}, {'id': 518707726, 'state': 'EXECUTED', 'date': '2018-11-29T07:18:23.941293', 'operationAmount': {'amount': '3348.98', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 3152479541115065', 'to': 'Visa Gold 9447344650495960'}, {'id': 542678139, 'state': 'EXECUTED', 'date': '2018-10-14T22:27:25.205631', 'operationAmount': {'amount': '90582.51', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 2256483756542539', 'to': 'Счет 78808375133947439319'}, {'id': 649467725, 'state': 'EXECUTED', 'date': '2018-04-14T19:35:28.978265', 'operationAmount': {'amount': '96995.73', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 27248529432547658655', 'to': 'Счет 97584898735659638967'}, {'id': 147815167, 'state': 'EXECUTED', 'date': '2018-01-26T15:40:13.413061', 'operationAmount': {'amount': '50870.71', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 4598300720424501', 'to': 'Счет 43597928997568165086'}]

    assert func.sorted_data(load_bank_data(os.path.join('test.json'))) == list_sorted


def test_date_change():
    assert func.date_change("2019-04-04T23:20:05.206878") == "04.04.2019"


def test_from_user():
    assert func.from_user(None) == "XXXX XXXX XXXX XXXX"
    assert func.from_user("Mastercard 1234561278901234") == "Mastercard 1234 56** **** 1234"


def test_to_user():
    assert func.to_user("Mastercard 1234564278904321") == "Mastercard **4321"


def test_show_transactions():
    assert func.show_transactions(None) == "ERROR 404"
