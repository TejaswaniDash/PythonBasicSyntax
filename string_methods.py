# Example to show available string methods in python
#accessing characters in a string
#string is sequence of characters and it  made up of multiple charater joined together

first="nyc"
print(first)

first="nyc"[0]
print(first)
first="nyc" [1]
print(first)
first="nyc"[2]
print(first)
#first="nyc"[3] #will give error since there is no character for index 3
#print(first)

first="nyc"[0]
city="sfo"
print(first)
ft=city[0] #we can access the 1st character of variable of city
print(ft)

#built in methods

"""
len()   #identifying the lenght of string
lower() 
upper()
str() # change non-string character to string
"""

stri= "ThIs Is a MixED Case"
print(stri.lower())
#this str.lower will change all the character to lower case

stri= "ThIs Is a MixED Case"
print(stri.upper())
#this str.upper will change all the character to upper case

stri= "ThIs Is a MixED Case"
print(len(stri))
#this slen(str) give the length of the string it also include the spaces as a character while counting

#print(stri +2) #if we want to add 2 at the end of the sentence/string
#this is wrong because it will give an integer error

#to add 2 at the end
print (stri + str(2))
#here str is an in built function of string is used thats why str(2) to add 2 at the end

#concatenation- adding 2 strings together

print("Hello" + " " + "World !!!")
print (first + " " + city)
#here i am emerging and adding both hello world and 1st character from first string i.e. n and city i.e. sfo
