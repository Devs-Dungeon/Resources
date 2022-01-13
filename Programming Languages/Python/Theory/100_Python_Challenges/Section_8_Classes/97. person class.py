'''
Create a method in the Person class which returns how another person's age compares. 
Given the objects p1, p2 and p3, which will be initialized with the attributes name and age, return a sentence in the following format: {other_person} is {older than / younger than / the same age as} me.

Examples :

p1 = Person("Nancy", 45)

p2 = Person("Maya", 36)

p3 = Person("Allen", 45)



Expected output:

p1.compare(p2)  ➞ "Maya is younger than me."

p2.compare(p1) ➞ "Nancy is older than me."

p1.compare(p3) ➞ "Allen is the same age as me."
'''

class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def compare(self,val):
        if self.age>val.age:
            print(f"{val.name} is younger than me.")
        elif self.age<val.age:
            print(f"{val.name} is older than me.")
        elif self.age==val.age:
            print(f"{val.name} is the same age as me.")

p1 = Person("Nancy", 45)

p2 = Person("Maya", 36)

p3 = Person("Allen", 45)


p1.compare(p2)
p2.compare(p1)
p1.compare(p3)
