"""
Example to show available string method in python
"""
#how to replace something in string?

a="1abc2abc3abc4abc"
#replace some pattern
print(a.replace("abc","ABC"))
#here (a.replace()) we are using to replace something to something
# here (a.replace("abc" , "ABC")- replacing abc to ABC

print (a.replace("abc","ABC",2))
#whatever count we give it will replace that much instances

#sub-string method
sub = a[1:6]
print ("************************")
print(sub)
#use of step
step = a[1:6:2]
#here it will print aca- it takes a then it skips1, then it takec and skips 1and so on till character6

print(step)

step = a[1:6:3]

print(step)