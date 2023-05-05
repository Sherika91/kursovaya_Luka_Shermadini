from datetime import datetime


def sorted_data(data):
    """Sorting data by the latest transactions made"""
    data = [trans for trans in data if trans]
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data


def date_change(data):
    """Method to change date on the one that's needed """
    date_changed = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
    return date_changed.strftime('%d.%m.%Y')


def from_user(item):
    """separating account transaction name account (sent from user) number to different
     lists and returning them covered so numbers are hidden"""
    if item is None:
        return "XXXX"
    else:
        split_string = item.split(' ')
        account_name = split_string[0]
        account_number = split_string[1]
        return f"{account_name} {account_number[0:4]} {account_number[4:6]}{'** ' + ('*' * 4)} {account_number[-4:]}"


def to_user(item):
    """separating account transaction name, account, number (received by user) to different
         string and returning them covered so numbers are hidden"""
    split_string = item.split(' ')
    account_name = split_string[0]
    account_number = split_string[1]
    return f"{account_name} {'*' * 2}{account_number[-4:]}"


def show_transactions(data):
    """inputing modified data that already have been modified, changed
     dates and outputting it the way bank widget needs it """
    if data is None:
        return "ERROR 404"
    for transaction in data[:5]:
        print("-" * 30)
        print('{date} {description}\n'
              '{from_} --> {to}\n'
              '{amount} {currency}\n'.format(date=date_change(transaction['date']),
                                             description=transaction['description'],
                                             from_=from_user(transaction.get('from')),
                                             to=to_user(transaction['to']),
                                             amount=transaction['operationAmount']['amount'],
                                             currency=transaction['operationAmount']['currency']['name'], )
              )
