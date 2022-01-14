#Name the file datetime.py and fix the error
import requests
print(__name__)

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])

print(__name__)
