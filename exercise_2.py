#fromkeys () method in  Dictionary

fruits = ("apple", "mango", "pineapple", "lemon", "kiwi", "grape")
vals = 1
my_fruits = dict.fromkeys(fruits, vals)
print(my_fruits)


#setdefault()
#it returns tha value of the item with the specified key

car = {
    "brand" : "Toyoto",
    "model" : "Camry",
    "year" : 1987
}

x = car.setdefault("model", "Hilux")
print(x)


#get ()
car = {
    "brand" : "Toyota",
    "model" : "Camry",
    "year" : 1987,
    (1,2,3) : 2
}

x = car.get("year")
print(x)
print(car[(1,2,3)])
