from dotenv import load_dotenv
import os
import requests

load_dotenv()
def convert_price(source, target, amount):
        API_KEY = os.getenv('API_KEY')
        URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{source}"
        try:
            response = requests.get(URL).json()
            currency_rate = response['conversion_rates'][target]
            return currency_rate * amount
        except KeyError:
            print("""
                This Currency is not available. You can check all supported currencies in this link : 
                https://www.exchangerate-api.com/docs/supported-currencies
                """)
            return None
        
while True:
    print("\nType 'q' at any prompt to quit the program.")
    
    source_currency = input("Source Currency (e.g., EUR): ").upper()
    if source_currency == 'Q':
        print("Exiting program. Goodbye!")
        break
    
    target_currency = input("Target Currency (e.g., USD): ").upper()
    if target_currency == 'Q':
        print("Exiting program. Goodbye!")
        break
    
    try:
        amount_input = input("Amount in EUR: ")
        if amount_input.upper() == 'Q':
            print("Exiting program. Goodbye!")
            break
        amount = float(amount_input)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        continue
        
        
    result = convert_price(source_currency, target_currency, amount)
    if result is not None:
        print(f"{amount} {source_currency} is equal to {result:.2f} {target_currency}")
        


