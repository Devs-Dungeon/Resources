#Add a new employee to the dictionary and print the dict out

from pprint import pprint

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))

pprint(d)
