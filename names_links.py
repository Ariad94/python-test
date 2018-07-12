def create_table(word):
	table = LinkTable()
	return table.file_of_links(word)

class Soup:
	def Div_g(self, word):
		import requests
		from bs4 import BeautifulSoup
		url_beggining = "https://www.google.es/search?q="
		response = requests.get(url_beggining + word)
		soup = BeautifulSoup(response.text, "html.parser")
		return soup.find_all("div", {"class":"g"})
		
class LinkTable:
	def file_of_links(self,word):
		anchors_names = LinkTable.filtered_names_list(self,"a",word)
		cites_names = LinkTable.filtered_names_list(self,"cite",word)
		counter = range(1,len(anchors_names))
		with open(word + ".txt", "w") as file:
			for i in counter:
				line = str(i)+"\t"+anchors_names[i]+"\t"+cites_names[i]+"\n"
				file.write(line)
	def names_list(self, tag, word):
		div_g = Soup().Div_g(word)
		div_g = [d for d in div_g if (d.find("a") and d.find("cite"))  is not  None]
		list = [] #list.append(d.find(tag) for d in div_g)
		for d in div_g:
			list.append(d.find(tag))
		list_names = []  #return list_names.append(l.text for l in list)
		for l in list:
			list_names.append(l.text)
		return list_names
	def filter_index(self,word):
		names_list = LinkTable.names_list(self,"cite",word)
		filter_index = []
		for c in names_list:
			if c[0:3] == "htt" or c[0:3] == "www": filter_index.append(names_list.index(c))
		return filter_index
	def filtered_names_list(self, tag, word):
		return [LinkTable.names_list(self,tag,word)[i] for i in LinkTable.filter_index(self,word)]
			
if __name__ == "__main__":  
	import sys 
	create_table(sys.argv[1])
