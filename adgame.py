# building an adjective game of python
number1 = input("Pick a number : ")
adjective1 = input("Pick an adjective 1 : ")
item = input("Pick an item : ")
place1 = input("Pick a place: ")
noun1 = input("Pick a noun : ")
adjective2 =input("Pick an adjective 2 : ")
text = (f"I was at {place1}, i had only $ {number1}, I want to buy a {item}, and I was {adjective1} and suprisly i met {noun1}, Wow that was {adjective2} meeting")        
print("-------------------")      
print(text)
# pratise dictionaries:
#📘 Question 1:
#Create a dictionary named student with this info:
#name: "Yasin"
#age: 20
#grade: "A"
dictionary = {"name":"Yasin","age":20,"grade":"A"}
car = {"brand": "Toyota", "year": 2020, "color": "blue"}
#How do you get the value of the "brand" key from the car dictionary
print(dir(dictionary))
