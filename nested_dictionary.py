"""
#NESTED DICTIONARY
d= {'k1':{'nestk1':'nestV1', 'nestk2':'nestV2', 'nestk3':'nestV3'}}
d['K1']['nestk1'] # if we want to access the nest key
"""

cars ={'bmw':{'model':'55Qi','year':'2021'}, 'benz':{'model':'E350','year':'2015'}} # here we stored all the information of bmw in one key
bmw_year= cars['bmw']['year']
#by providing the key we are accessing the value
print(bmw_year)
print( cars['benz']['model'])



