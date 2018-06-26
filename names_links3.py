def __main__(word):
	return LinkTable(word)


class LinkTable: 
	import requests 
	from bs4 import BeautifulSoup
	def __init__(self, word):
		url_beggining = "https://www.google.es/search?q=" 
		response = requests.get(url_beggining + word) 
		soup = BeautifulSoup(response.text, "html.parser")
		div_g = soup.find_all("div", {"class":"g"})
		self.div_g = [d for d in div_g if (d.find("a") and d.find("cite"))  is not  None]
		anchors_names = LinkTable.filtered_names_list(self,"a")
		cites_names = LinkTable.filtered_names_list(self,"cite")
		counter = range(len(anchors_names))
		with open(word + ".txt", "w") as file: 
			for i in counter:
				file.write(i+1,"\t",anchors_names[i],"\t",cite_names[i])
	def names_list(self, tag):
		list = []
		#list.append(d.find(tag) for d in LinkTable.div_g)
		for d in LinkTable.div_g:
			list.append(d.find(tag))
		list_names = []
		#return list_names.append(l.text for l in list)
		for l in list:
			list_names.append(l.text)
		return list_names
	def filter_index(self):
		filter_index = []
		for c in LinkTable.names_list(self,"cite"):
			if c.text[0:3] == "htt" or c.text[0:3] == "www": index.append(cites_names.index(c))
		return filter_index
	def filtered_names_list(self,tag):
		return [LinkTable.names_list(tag)[i] for i in LinkTable.filter_index(self)]
			
if __name__ == "__main__":  
	import sys 
	search(sys.argv[1]) 


 


 
 
 
 
 

 
 
 
 



