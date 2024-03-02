"""
List Data Type
#used to store more than value in one variable name
list items are in brackets, seperated with "," [1,2,3,]

"""
cars = ["bmw","audi","honda"]
emptylist =[]
print(cars)
print(emptylist)
#here since empty list don't have any value it will give back only brackets no values

#ACCESSS ELEMENTS INSIDE THE LIST
#using index

print("*#"*20)

print(cars[0])

print("*#"*20)

print(cars[1])

print("*#"*20)

print(cars[2])

num_list =[1,2,3]
sum_num= num_list[0]+num_list[1]
print(sum_num)
#we can access the values in the list using the index number for ex- cars[0]=bmw, cars[1]=audi so on

more_cars = ["bmw","audi","honda"]
print(more_cars[1])

#we can also assign values to indexes in list for example more_cars[1] here will be Audi
#but what if we assign a value to more_cars[1]

more_cars[1]="Benz"
print(more_cars[1])
#now print(more_cars[1]) will give benz not audi
#let's print everything
print(more_cars) #here we can see benz replaced audi because we assigned the index1 value as benz
