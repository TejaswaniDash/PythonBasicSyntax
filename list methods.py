"""
Built in methods to help manipulating a list
"""

cars = ["bmw","audi","honda"]

# len() #give lenth of the cars

length=len(cars)
print(length)

#what if we decided we don't want only 3 cars in that case we can append the items in the list using append()
#append will add the appended names in the end of the original list
#list.append() takes exactly one argument (4 given)
#cars.append("benz","tata","Q4","suv")
cars.append("Benz")
print(cars)

#lets add some more cars to the list in desired place rather than adding them at the end
#for this we use list.insert()
#list.insert for this we have to enter the desired index where we want to add the item

cars.insert(1,"jeep")
print(cars)

#find index of particular item in the list

x= cars.index("honda")
print(x)

#how we can remove a item from a list we use list.pop()
y= cars.pop()
print(y)
#it will remove the last item of the list
#by default pops remove the last iteam
print(cars)

#lets remove something from the list in desired place rather than removing from the end
#for this we use list.remove()

cars.remove("jeep")
print(cars)

#slicing alist

slicing = cars[0:2]
print(slicing)

slicing = cars[1:]
print(slicing)

slicing = cars[0:2]
a= cars[2:]
print(a)

#let's sort the list
#alphabetical sorting
print("*#"*20)
print(cars)
cars.sort() #we have to sort out the list out of the print
print(cars)