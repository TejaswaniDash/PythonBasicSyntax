"""
Dictionary methods
"""

car= {'make':'bmw', 'model':'5Qi','year':'2021'}
cars ={'bmw':{'model':'55Qi','year':'2021'}, 'benz':{'model':'E350','year':'2015'}}
print(car.keys())
#dictionary.key() will run all the keys that the dictionary contains
print(cars.keys())
print(car.values()) #dictionary.values() will run all the values that the dictionary contains
print(cars.values())

#if we want to see all the items i.e. keys and values all we can ue dict.items()

print(car.items())
print(cars.items())

#let's copy a dictionary
car_copy =car.copy()
print(car_copy)

#to clear the dictionary we can use dict.clear()

#car.clear()
#print(car) #it will give an empty outcome as we clear everything in dictionary car

print (car.pop('model')) #to remove certain selected iteam from the dictionary we can use dict.pop()
print(car)
