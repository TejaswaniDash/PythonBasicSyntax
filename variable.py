

#table
#object reference count

a="NYC"
b="NYC"

a=123
#now a now points to object 123 not NYC and count for NYC decrese from 2 to 1

print(a)
print(b)
#when reference count become zero with respect to NYC here then python will handover this NYC object to garbage collector and manage the space
c='NYC'
d=c
print(c==d)
print(c is d)
import keyword
print(keyword.kwlist)
#here import can't be used as a variable as import is something like importing a package and module
#here keyword is a module, it's like a class or library built by python

a=b=c=10
print(a)
print(b)
print(c)
#we can assign and define variables in 1 line

x,y,z=10,20,30
print(x)
print(y)
print(z)
#here by using comma we seperated the values with respect to the identifiers x,y,z



