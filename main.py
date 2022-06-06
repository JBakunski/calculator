import logging
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
    number_1 = int((input("Podaj pierwszą liczbę: ")))
    number_2 = int((input("Podaj drugą liczbę: ")))

    if operation == '1':
        output = addition
    elif operation == '2':
        output = subtraction
    elif operation == '3':
       output = multiplication
    elif operation == '4':
        output = division
    
    print_result(output(number_1, number_2))

if __name__ == "__main__":
    perform_calculation(select_operation())