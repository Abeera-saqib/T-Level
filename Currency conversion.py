""" Sharma loves to travel in different countries and he uses different currencies in different countries. Sometime he gets confused related to the conversation of the money. So to help Sharma write a program in python with functions that can take three parameters: amount, from_currency(currency that has to be converted), to_currency(currency in which it has to be converted). The function should return the amount after conversion. The program should contain at least four different types fo currencies. """

def convert_currency(amount, from_currency, to_currency):
    """
    Convert currency from one type to another.
    
    Args:
    - amount: float, amount to be converted
    - from_currency: string, currency code to convert from
    - to_currency: string, currency code to convert to
    
    Returns:
    - float, converted amount
    """
    # Define exchange rates manually
    exchange_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.73, 'JPY': 111.21},
        'EUR': {'USD': 1.18, 'GBP': 0.86, 'JPY': 129.78},
        'GBP': {'USD': 1.37, 'EUR': 1.16, 'JPY': 151.29},
        'JPY': {'USD': 0.0090, 'EUR': 0.0077, 'GBP': 0.0066}
    }
    
    # Check if currencies are in the exchange rates dictionary
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        conversion_rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Conversion not available for the given currencies"

def main():
    amount = float(input("Enter amount to convert: "))
    from_currency = input("Enter currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter currency to convert to (e.g., EUR): ").upper()
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
