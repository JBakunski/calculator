import sys, logging
from decimal import Decimal

logging.basicConfig(level=logging.INFO)


def select_operation():
    output = input("""Wybierz działanie, które chcesz wykonać:
    [1] Dodawanie
    [2] Odejmowanie
    [3] Mnożenie
    [4] Dzielenie\n""")
    return output


def addition(number_1, number_2):
    result = number_1 + number_2
    logging.info(f"Dodaję {number_1} i {number_2}")
    return result

def subtraction(number_1, number_2):
    result = number_1 - number_2
    logging.info(f"Odejmuję {number_2} od {number_1}")
    return result

def multiplication(number_1, number_2):
    result = number_1 * number_2
    logging.info(f"Mnożę {number_1} przez {number_2}")
    return result

def division(number_1, number_2):
    result = number_1 / number_2
    logging.info(f"Dzielę {number_1} przez {number_2}")
    return result

def print_result(result):
    print(f"Wynik to {result}")


def perform_calculation(operation):
    number_1 = Decimal(input("Podaj pierwszą liczbę: "))
    number_2 = Decimal(input("Podaj drugą liczbę: "))

    if operation == '1':
        print_result(addition(number_1, number_2))
    elif operation == '2':
        print_result(subtraction(number_1, number_2))
    elif operation == '3':
        print_result(multiplication(number_1, number_2))
    elif operation == '4':
       print_result(division(number_1, number_2))

if __name__ == "__main__":
    perform_calculation(select_operation())