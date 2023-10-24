from token_key import get_currencies


# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 7. Вывод результата

token_key = get_currencies()

def greeting():
    
    print("\n\tПривет, это программа Конвертер Валют!")

    print(f"""
        Для работы с программой требуется:
        - выбрать исходную валюту 
        - выбрать в какую валюту следует перевести
        - ввести количество исходной валюты

        Доступные валюты:
        """)    
    
def convert(amount, from_ticker, to_ticker, token_key):
    
    from_ticker = token_key['data'].get(from_ticker)  # исходная валюта
    to_ticker = token_key['data'].get(to_ticker)  # в какую переводим

    coefficient = to_ticker / from_ticker
    return round(amount * coefficient, 2)  # возвращаем результат подсчета


def input_currency(input_message, token_key):
    
    ticker = input(f"{input_message} > ").strip().upper() # не стал заморачиваться с регистрами
    
    currency = token_key.get(ticker, None)  # поиск валюты в словаре
    if currency is None:  # случай в котором не была найдена валюта
        while currency is None:
            ticker = input(f"Данная валюта не была обнаружена. Попробуйте снова > ").strip().upper()
            currency = token_key.get(ticker, None)

    return ticker
    

def currency_request():
    
    print(f"\t{"*" * 25}")
    
    for currency in token_key['data']:  # вывод всех имеющихся валют
        print(f'\t*\t- {currency}\t\t*')
        
    print(f"\t{"*" * 25}")

    from_ticker = input_currency("\nВведите исходную валюту", token_key['data'])
    to_ticker = input_currency("Введите в какую валюту следует перевести", token_key['data'])

    amount_input = input("Введите количество валюты: ")  # ввод количества валюты

    if '.' in amount_input:  # проверка является ли введенное количество целым числом или вещественным
        amount = float(amount_input)
    else:
        amount = int(amount_input)

    result = convert(amount, from_ticker, to_ticker, token_key)

    print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')


def main():
    greeting()
    currency_request()
    
if __name__ == '__main__':
    main()
