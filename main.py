
from decimal import Decimal


def select_operation():
    output = input("""Wybierz działanie, które chcesz wykonać:
    [1] Dodawanie
    [2] Odejmowanie
    [3] Mnożenie
    [4] Dzielenie\n""")
    return output

def addition(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def get_numbers():
    number_1 = Decimal(input("Podaj pierwszą liczbę: "))
    number_2 = Decimal(input("Podaj drugą liczbę: "))
    return number_1, number_2


if select_operation() == '1':
    result = addition(get_numbers())
    print(f"Twój wynik dodawania wynosi: {result}")