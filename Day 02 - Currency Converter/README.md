# Currency Converter Project

A Python-based currency converter that uses the [ExchangeRate-API](https://app.exchangerate-api.com) to fetch real-time exchange rates. This project allows users to convert amounts between currencies interactively, with error handling for invalid inputs.

Features
• Fetches live exchange rates from [ExchangeRate-API](https://app.exchangerate-api.com).
• Converts amounts between currencies dynamically.
• Provides error handling for unsupported currencies or invalid inputs.
• Supports interactive quitting of the program.

Prerequisites
• Python 3.x installed on your system.
• An API key from [ExchangeRate-API](https://app.exchangerate-api.com).

Setup Instructions

Step 1: Clone the Repository

Step 2: Install Dependencies

Install the required Python libraries from the requirements.txt file:

pip install -r requirements.txt

Step 3: Create a .env File

In the project directory, create a .env file and add your API key in the following format:

API_KEY=your_api_key_here

Step 4: Run the Program

Use the following command to run the script:

python currency_converter.py

How to Use 1. Enter the source currency (e.g., EUR). 2. Enter the target currency (e.g., USD). 3. Provide the amount to convert. 4. The program will output the equivalent value in the target currency.

Example

```
Source Currency (e.g., EUR): EUR
Target Currency (e.g., USD): USD
Amount in EUR: 20
20 EUR is equal to 21.84 USD
```

Notes
• Ensure your .env file is in the same directory as the script.
• Do not share your API key publicly; keep it secure in the .env file.
• For a list of supported currencies, refer to the [ExchangeRate-API](https://www.exchangerate-api.com/docs/supported-currencies) documentation.
