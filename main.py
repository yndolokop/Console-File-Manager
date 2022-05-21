import os
import shutil
import sys
import pickle


from my_bank_account import buy, shopping_history
from victorina_famous_people import get_person_and_question


def console_file_manager():
    while True:
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. мой банковский счет')
        print('10. играть в викторину')
        print('11. смена рабочей директории')
        print('12. выход')
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            folder = input('Введите имя папки: ')
            os.mkdir(f'{folder}')
        elif choice == '2':
            folder = input('Введите имя папки: ')
            os.rmdir(f'{folder}')
        elif choice == '3':
            original = input('file name ')
            target = input('file name ')
            original = os.path.join(os.getcwd(), f'{original}')
            target = os.path.join(os.getcwd(), f'{target}')
            shutil.copy(original, target)
        elif choice == '4':
            print(os.listdir())
        elif choice == '5':
            for i in os.listdir(os.path.join(os.getcwd())):
                if os.path.isdir(i):
                    print(i)
        elif choice == '6':
            for i in os.listdir(os.path.join(os.getcwd())):
                if os.path.isfile(i):
                    print(i)
        elif choice == '7':
            print(sys.platform)
        elif choice == '8':
            print(sys.exit('Python creator Guido van Rossum sys.exit()s as language overlord'))
        elif choice == '9':
            if os.path.exists('shopping_history.data'):
                with open('shopping_history.data', 'rb') as f:
                    pickle.load(f)
            new_balance = 0
            while True:
                print('1. пополнение счета')
                print('2. покупка')
                print('3. история покупок')
                print('4. выход')
                print(f'Ваш счет: {new_balance}')
                choice = input('Выберите пункт меню: ')
                if choice == '1':
                    balance = int(input('Пополните счет. Введите сумму пополнения: '))
                    new_balance += balance
                elif choice == '2':
                    price = int(input('Введите сумму покупки: '))
                    new_balance = buy(new_balance, price)
                elif choice == '3':
                    shopping_history()
                    print('История покупок: ', shopping_history())
                elif choice == '4':
                    with open('shopping_history.data', 'wb') as f:
                        pickle.dump(shopping_history(), f)
                    break
                else:
                    print('Неверный пункт меню')
        elif choice == '10':
            rounds = int(input('Сколько раз вы хотите играть? '))
            for i in range(rounds):
                get_person_and_question()
            print('Пока!')
        elif choice == '11':
            os.chdir(os.path.join(os.getcwd(), input('Введите имя директории: ')))
            print(os.getcwd())
        elif choice == '12':
            break
        else:
            print('Неверный пункт меню')


console_file_manager()