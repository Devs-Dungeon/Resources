#Count how many a the text file has
import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
count_a = text.count("a")
print(count_a)
