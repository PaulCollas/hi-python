########### KURRENCY ###############

# IMPORT REQUESTS
import requests

class Currency_convertor:

	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()

		# TAKE JUST VALUES WHO NEEDED
		self.rates = data["rates"]

	# FONCTION FOR MAKE CROSS FUNCTION FROM FROM / TO / AMOUNT
	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		# LIMIT FOR 2 CARACT
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))



if __name__ == "__main__":
  
	# OWN KEY FROM FIXER
    key = 'c2d686057a0b19d27f54b4a529b3b652'

	# URL FROM API
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', key)

	# MAGIC FUNCTION TO CONVERT  
    c = Currency_convertor(url)

	# EXPLAIN + INPUT
    print('Choisir un format de monnaie parmi : "USD", "JPY", "GBP", "CNY", "CHF", "CAD", "AUD"')
    from_country = input("A partir de quelle monnaie: ")
    to_country = input("Pour quelle monnaie: ")
    amount = int(input("Quel montant: "))
  
    c.convert(from_country, to_country, amount)