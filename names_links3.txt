def create_link_table:
	anchors_names = LinkTable.filtered_names_list("a")
	cites_names = Link.Table.filtered_names_list("cite")
	counter = range(len(anchors_names))
	with open(word + ".txt", "w") as file: 
		for i in counter:
			file.write(i+1\tanchors_names[i]\tcite_names[i]) 


class LinkTable(word):

	import requests 
	from bs4 import BeautifulSoup 

	url_beggining = "https://www.google.es/search?q=" 
	response = requests.get(url_beggining + word) 
	soup = BeautifulSoup(response.text, "html.parser")
	
	div_g = soup.find_all("div", {"class":"g"})
	div_g = [d for d in div_g if (d.find("a") and d.find("cite"))  is not  None]
	
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
		
	cites_names = Link.Table.names_list("cite")
	
	filter_index = []
	for c in cites_names:
		if c.text[0:3] == "htt" or c.text[0:3] == "www": index.append(cites_names.index(c))
	
			
		
	def filtered_names_list(self,tag):
		return [LinkTable.names_list(tag)[i] for i in filter_index] 
		
if __name__ == "__main__":  
	import sys 
	search(sys.argv[1]) 


 


 
 
 
 
 

 
 
 
 



