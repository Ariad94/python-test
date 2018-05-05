def search(word):
  file = open(word + ".html", "w")
  url_beggining = "https://www.google.es/search?q="
  import requests
  url = requests.get(url_beggining + word)
  file.write(url.text)
  file.close()

if __name__ == "__main__": 
  import sys
  search(sys.argv[1])
  
