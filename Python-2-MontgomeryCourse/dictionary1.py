# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:01:12 2019

@author: GBTC441005UR
"""

# strings as keys and values
countries = {"CA": "Canada",
             "US": "United States",
             "MX": "Mexico"}

# numbers as keys, strings as values
numbers = {1: "One", 2: "Two", 3: "Three", 
           4: "Four", 5: "Five"}

# strings as keys, values of mixed types
movie = {"name": "The Holy Grail", 
         "year": 1975,
         "price": 9.99}

# an empty dictionary
book_catalog = {}


countries["GB"]="United Kingdom"
countries["FR"]="France"

print(countries)

country=countries.get("MX")
print(country)

del countries["MX"]
del countries["MX"]

code="IE"
if code in countries:
    country=countries[code]
    del countries[code]