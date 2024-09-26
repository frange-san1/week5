# collection + single "variable" used to store multiple values
#  list = [] ordered and changeable. Duplicates OK. 
#  set= {} unordered and immutable, but Add/Remove OK. NO duplicates
#  Tuble = () ordered and unchangeable. Duplicates OK. Faster 

fruits = ["apple", "orange", "banana", "coconut", "pineapple",]
# print(fruits[])
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[0] = "pineapple" # I can reassing values using this
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits .clear()

#print(fruits.index("coconut"))

#print(fruits)

# print(fruits[0])
# for fruit in fruits:
#    print(fruit)

cars = ["bmw", "maserati", "audi", "mercedes", "ferrari"]
print(f"these are list of {cars}")
print(f"the first car is {cars[0]}")


#changing the vaule of the list
cars[0]= "toyota"
print(f"the first car is {cars[0]}")


print(f"the last car is {cars[-1]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")

#adding a value to the list
cars.append("bugatti")
print(cars)

cars.remove("maserati")
print(cars)

# looping through the list 
# otherwise called iterating through the list 
for car in cars:
   # print(len(car))
    #print(car)
    carRequest = input("add a new car please: ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)
    if len(cars) > 10:
        break 