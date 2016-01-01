import Quandl
import pandas as pd
from bs4 import BeautifulSoup

api_key = open('quandlapikey.txt','r').read()
df = Quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head())

fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
#This is a list from https://simple.wikipedia.org/wiki/List_of_U.S._states
print(fiddy_states)

#This is a dataframe from https://simple.wikipedia.org/wiki/List_of_U.S._states
print(fiddy_states[0])

#This is a column from https://simple.wikipedia.org/wiki/List_of_U.S._states
print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))