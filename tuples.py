"""
#similar to list but they are inmutable
it means you can't change them
"""
my_list =[1,2,3]
print(my_list)

my_list[0]=0
print(my_list)
#above are list we can change but tuples we can't change
#only difference between list and tuple is the parenthesis

my_tuple =(1,2,3)
print(my_tuple)

#my_tuple[0]=0
#print(my_tuple) # we will get error - 'tuple' object does not support item assignment
#we said tuple is similar to list what does that mean?
#it means that we can access elements as we do in list

print(my_tuple[0])

#we can do slicing as well in touple
print(my_tuple[1:])
print(my_tuple[0:])
print(my_tuple[:2])

#limited method provide in touple
# first method:- find the index of the item in touple

print(my_tuple.index(1))
print(my_tuple.index(3))

# second method:- count - it counts the number of time the paticular item appears in touple
print(my_tuple.count(1))
my_tuple1= (0,1,1,1,2,2,2,2,2,3,4,5,6,6,7,7,8,8,8,8)
print(my_tuple1.count(1))
print(my_tuple1.count(8))