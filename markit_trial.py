import requests

lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

def company_search(string):
	r = requests.get(lookup_url+string)
	print(r)
	try:
		return r.json()
	except ValueError:
		return 0

def get_quote(string):
		r = requests.get(quote_url+string)
		try:
		#r.json().get("LastPrice"):
			return r.json() #.get("LastPrice")
		except ValueError:
			return 0
company_search("AAPL")
print(get_quote("AAPL"))