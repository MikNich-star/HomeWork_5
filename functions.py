import random
import os
import os.path

famous = {'А.П.Чехов': '29.01.1860', 'П.И.Чайковский': '07.05.1840', 'Д.И.Менделеев': '08.02.1834',
          'А.Н.Толстой': '09.09.1828', 'Ф.М.Достоевский': '11.11.1821', 'Н.И.Пирогов': '25.11.1810',
          'А.С.Пушкин': '26.05.1799', 'В.И.Вернадский': '28.02.1863', 'В.И.Ленин': '22.04.1870',
          'И.В.Сталин': '06.12.1878'}


def game():
    total = 10
    score = 0
    while total > 0:
        answer = str(input('Дата рождения ' + random.choice(list(famous.keys())) + ':'))
        if total == 6:
            break
        total -= 1
        for i, j in famous.items():
            if answer == j:
                score += 1
    print('Количество правильных ответов :', score)
    if score < 2:
        print('Плохой результат , подготовься и приходи снова .')
    elif 2 < score <= 4:
        print('Хорошо, попробуй еще раз ')
    else:
        print('Отличный результат !!!')


def bill_fun():
    buy_list = []
    cash_balans = 0
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('БАЛАНС :', cash_balans)
        choice = input('Выберите пункт меню')
        if choice == '1':
            sum_balans = int(input('Введите сумму на которую хотите пополнить счет:'))
            cash_balans += sum_balans

        elif choice == '2':
            buy = int(input('Введите сумму покупки:'))
            if buy > cash_balans:
                print('На вашем балансе недостаточно средств')
            else:
                cash_balans -= buy
                name = input('Ведите название покупки:')
                buy_list.append((name, buy))
        elif choice == '3':
            print(buy_list)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


def show_files():
    files_list = []
    for el in os.listdir(os.getcwd()):
        if not os.path.isdir(os.path.join('.', el)):
            files_list.append(el)
    return files_list
