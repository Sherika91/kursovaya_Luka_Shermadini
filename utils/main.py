from data_for_widget import load_bank_data
import func
import os.path

DATA_FROM_BANK = os.path.join('../operations.json')


def main():
    # getting EXECUTED list of transactions
    exe_list = load_bank_data(DATA_FROM_BANK)

    # sending loaded data to sorting by latest transaction made
    exe_sorted_by_date = func.sorted_data(exe_list)

    """ Final act, sending all the data that we formed to main function for pars reformat of datatime from
    Y% %m %d to d% %m %Y"""
    func.show_transactions(exe_sorted_by_date)
    # returning last 5 transactions made by the user to the widget app
    # all sorted, Reformed and filtered out by EXECUTED


if __name__ == '__main__':
    main()
