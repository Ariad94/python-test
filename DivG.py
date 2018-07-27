import requests
from bs4 import BeautifulSoup
		
class DivG:

	# Explicar funcionalidad
	
	def list(self, word):
		url_start = "https://www.google.es/search?q="
		url = requests.get(url_start + word)
		html_text = BeautifulSoup(response.text, "html.parser")
		return html_text.find_all("div", {"class":"g"})