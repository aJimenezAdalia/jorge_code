

import requests
from datetime import datetime


class CurrencyConverter:
	"""Converts any currency."""
	def __init__(self, currency_1: str, currency_2: str):
		"""Class constructor. Receives the currencies that the user wants to convert.

		Params:
			- currency_1: str expected, first currency.
			- currency_2: str expected, second currency.
		"""
		self.currency_1 = currency_1.upper()
		self.currency_2 = currency_2.upper()
		self.url = "https://alpha-vantage.p.rapidapi.com/query"
		self.today = datetime.today().strftime('%Y-%m-%d')

		self.querystring = {
			"from_symbol": self.currency_1,
			"function": "FX_DAILY",
			"to_symbol": self.currency_2,
			"outputsize": "compact",
			"datatype": "json"}

		self.headers = {
			"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
			"X-RapidAPI-Key": "1ca795b67amshfa6cf81e0962bf1p1e245ajsn33f3f8989a97"}

	def get_json_response(self) -> dict:
		"""Return a JSON object with the received data from the API."""
		try:
			response = requests.request(
				"GET",
				self.url,
				headers=self.headers,
				params=self.querystring)
			response_json = response.json()

			return response_json
		except Exception as e:
			print(e)

	def today_price(self) -> float:
		"""Return the current exchange price of both currencies."""
		try:
			response_json = self.get_json_response()
			daily_prices = response_json.get('Time Series FX (Daily)')

			current_price = float(daily_prices.get(self.today).get('1. open'))

			return current_price
		except Exception as e:
			print(e)


if __name__ == "__main__":
	first_currency = input('Choose the first currency (i.e. EUR, USD, GBP, etc...)\n')
	second_currency = input('Choose the second currency (i.e. EUR, USD, GBP, etc...)\n')

	currency_converter_object = CurrencyConverter(
		currency_1=first_currency,
		currency_2=second_currency)

	today_price = currency_converter_object.today_price()

	print(f'Price for {currency_converter_object.today}:\n')
	print(f'1 {first_currency.upper()} = {today_price} {second_currency.upper()}')
