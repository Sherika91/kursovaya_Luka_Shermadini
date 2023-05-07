import json


def load_bank_data(data):
    """ importing data of all transactions from file 'operators.json' """

    with open(data, 'r', encoding='utf-8') as file:
        data = json.load(file)
    executed_list = []
    for file in data:
        if file.get('state') == 'EXECUTED':
            executed_list.append(file)
        elif file.get('state') == 'FAILED':
            return 'Status Failed'
    return executed_list
