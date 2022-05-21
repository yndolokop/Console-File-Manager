history_item = []  # хранит историю товаров
history_price = []  # хранит историю цен
new_balance = 0


def shopping_history():  # функция печатает историю покупок из двух списков: названий товара и цен
    dict_history = dict(zip(history_item, history_price))
    return dict_history


def buy(new_balance, price):
    if price > new_balance:
        print('Недостаточно денег. Пополните счет')
    elif price <= new_balance:
        item_name = input('Введите название товара: ')
        new_balance -= price
        print('Остаток на счету: ', new_balance)
        history_item.append(item_name)
        history_price.append(price)
        print('Список покупок: ', history_item)
    else:
        print('Обратитесь в техподдержку')
    return new_balance



