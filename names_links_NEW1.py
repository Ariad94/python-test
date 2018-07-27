#Cargar archivo DivG
#Cargar archivo NamesAndLinks

def names_and_links_table(word):
	names_and_links = NamesAndLinks(word)
	names_column = names_and_links.list[:,1]
	links_column = names_and_links.list[:,2]
	with open(word + ".txt", "w") as file:
		for i in range(1,len(column_1)):
			line = str(i) + "\t" + names_column[i] + "\t" + links_column[i] + "\n"
			file.write(line)


if __name__ == "__main__":  
	import sys 
	names_and_links_table(sys.argv[1])
