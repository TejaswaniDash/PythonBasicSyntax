###Exmples to show strings works in python
#it's a sequence of character- ab,c,d or alphanumeric or special character,
# #when we define we have to put it in double or single quotes

a= "this is simple string"
b= 'using sing quotes'

print(a)
print(b)

#these are simple strings without apostophy or anything let's see complex strings

#c= "Need to use "quotes" inside a string"
#here python will not recognise it because so many quotes used that's why we use single quotes in here to define it
c= "Need to use 'quotes' inside a string"

print(c)
d= 'Need to use "quotes" inside the string' #vice- a versa
print(d)
e ="Another way to handel \"quotes\""
#here we used back slash to ignore the functionality of double quotes
#it will print the double quotes as it not use it's functionality
print(e)

f= "this is a single\
string"
#here let's say string is too long and want to split it to next line use backslash it will not treat
# it as next line ; it will treat as single line
print(f)




