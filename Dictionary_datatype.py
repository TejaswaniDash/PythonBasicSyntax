"""
#Data type to store more than one value in one variable name
#dictionary items are in brackets{} in terms of key value pairs, seperated with ","
# {"k1":"V1","k2":"v2","k3":"v3","k4":"v4"}
#value in a dictionary can be of any datatype.Another dictionary can be also a value
#not sequenced , no indexing
#worked on mapping
#mapping is key value
"""

car= {'make':'bmw', 'model':'5Qi','year':'2021'}
print(car)
#how can we access any item from dictionary?

#print(car[0]) #it will give error because dictionary don't work on index basis

print(car['make'])  #we have to give a key to print desired outcome from dictionary
print(car['model'])
print(car['year'])
#print(car['model1'])#if any key that doesn't exist in dictionary will give error

#empty dictionary
d={}
print(d)

#how we can add more items to a dictionary

d['one']=1
d['two']=2
print(d)

#let's do some operations in dictionary

sum_1= d['two'] +8
print(sum_1)
print(d)
#we can also change the value
d['two']= d['two'] +8
print(d)