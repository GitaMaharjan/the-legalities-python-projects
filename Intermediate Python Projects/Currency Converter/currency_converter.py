# 24.  Currency Converter   
#     *Description*: Build a program that converts one currency to another using static exchange rates.  
#     *Skills*: User input, conditionals, basic math.

class CurrencyConverter:
    def __init__(self):
        # Initialize the exchange rates (static values)
        self.exchange_rates = {
            'USD': 1.0,  # Base currency (USD)
            'EUR': 0.85,
            'GBP': 0.75,
            'JPY': 110.0,
            'INR': 73.0,
        }
    
    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency code.")
        
        # Convert the amount to USD, then to the target currency
        amount_in_usd = amount / self.exchange_rates[from_currency]
        converted_amount = amount_in_usd * self.exchange_rates[to_currency]
        return converted_amount


def main():
    converter = CurrencyConverter()
    
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency to convert from (USD, EUR, GBP, JPY, INR): ").upper()
        to_currency = input("Enter the currency to convert to (USD, EUR, GBP, JPY, INR): ").upper()

        # Validation to check if the same currency is used for conversion
        if from_currency == to_currency:
            print("You cannot convert the same currency. Please choose different currencies.")
            return
        
        converted_amount = converter.convert(amount, from_currency, to_currency)
        
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
