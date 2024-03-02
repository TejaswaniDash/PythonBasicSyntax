"""
Example to show available string method in python
"""
city="NYC"
event="music show"
print("Welcome to" + city + " and enjoy the " + event)
#ist way of concatenating but it's bit complicated with so many plus sign

#second method
print("Welcome to %s and enjoy the %s" %(city, event))
#here we use % sign for missing value % sign are place holder
#% sign operator will replace the %s of that string with the string variable that come after it
#Number of% sign should match to number variable needs to fill up

print("Welcome to %s" % city)