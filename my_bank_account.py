import pickle
import os
from filemanager import add_separators


@add_separators
def run_my_bank_account():
    new_balance = 0
    history_orders_list = []
    history_balance = []
    if os.path.exists('shopping_history.data'):
        with open('shopping_history.data', 'rb') as f:
            history_orders_list = pickle.load(f)
    if os.path.exists('shopping_history.data'):
        with open('new_balance_history.data', 'rb') as f:
            new_balance = pickle.load(f)
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'У Вас на счету: ', new_balance)
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = int(input('Пополните счет. Введите сумму пополнения: '))
            new_balance += balance
        elif choice == '2':
            price = int(input('Введите сумму покупки: '))
            if price > new_balance:
                print('Недостаточно денег. Пополните счет')
            elif price <= new_balance:
                item_name = input('Введите название товара: ')
                new_balance -= price
                print('Остаток на счету: ', new_balance)
                order = (price, item_name)
                history_orders_list.append(order)
                history_balance.append(new_balance)
                print('Список покупок: ', history_orders_list)
        elif choice == '3':
            print('История покупок: ', history_orders_list)
        elif choice == '4':
            with open('shopping_history.data', 'wb') as f:
                pickle.dump(history_orders_list, f)
            with open('new_balance_history.data', 'wb') as f:
                pickle.dump(new_balance, f)
            break
        else:
            print('Неверный пункт меню')
