import requests

def search(word):
  url_beggining = "https://www.google.es/search?q="
  response = requests.get(url_beggining + word)
  with open(word + ".html", "w") as file:
    file.write(response.text)
    
if __name__ == "__main__": 
  import sys
  search(sys.argv[1])
  
