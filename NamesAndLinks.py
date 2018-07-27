class NamesAndLinks:
	# Explicar funcionalidad
	
	div_list = DivG().list(word)
	div_with_a_and_cite = [div for div in div_list if (d.find("a") and d.find("cite"))  is not  None]
		
	def list(self):
		names_and_links_list = []
		for div in div_with_a_and_cite:
			cite = div.find("cite").text 
			cite_is_a_link = cite[0:4] == "http" or cite[0:3] == "www"
			if cite_is_a_link:
				names_and_links_list.append([div.find("a").text,div.find("cite").text])
		return names_and_links_list			