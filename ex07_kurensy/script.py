########### KURRENCY ###############

# Import the modules needed
import requests

class Currency_convertor:
	# empty dict to store the conversion rates
	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()

		# Extracting only the rates from the json data
		self.rates = data["rates"]

	# function to do a simple cross multiplication between
	# the amount and the conversion rates
	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		# limiting the precision to 2 decimal places
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))




# Driver code
# if __name__ == "__main__":

# 	key = 'c2d686057a0b19d27f54b4a529b3b652'
# 	url = str.__add__('http://data.fixer.io/api/latest?access_key=', key)
# 	c = Currency_convertor(url)

#     # allCountry = ['USD', 'JPY', 'GBP', 'CNY', 'CHF', 'CAD', 'AUD']

#     from_country = input("Choisir un type de monnaie [USD, JPY, GBP, CNY, CHF, CAD, AUD]:")
#     # if from_country not in allCountry:
#     #     print('choisir un format de monnaie valide')

# 	to_country = input("Choisir un type de monnaie:")
#     # if to_country not in allCountry :
#     #     print('choisir un format de monnaie valide')
#     #     print('Voici tout les types de monnaie valide : "USD", "JPY", "GBP", "CNY", "CHF", "CAD", "AUD" ')
# 	amount = int(input("Montant: "))
#     # if type(amount) != int  :
#     #     print('Le montant n\'est pas un nombre')

# 	c.convert(from_country, to_country, amount)



# Driver code
if __name__ == "__main__":
  
    key = 'c2d686057a0b19d27f54b4a529b3b652'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', key)  
    c = Currency_convertor(url)
    print('Choisir un format de monnaie parmi : "USD", "JPY", "GBP", "CNY", "CHF", "CAD", "AUD"')
    from_country = input("A partir de quelle monnaie: ")
    to_country = input("Pour quelle monnaie: ")
    amount = int(input("Quel montant: "))
  
    c.convert(from_country, to_country, amount)