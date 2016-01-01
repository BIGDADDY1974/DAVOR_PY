import pandas as pd

df1 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})


df3 = pd.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})

print (df1)
print (df3)
merged = pd.merge(df1,df3, on="Year", how = "right")
merged.set_index("Year", inplace=True)
print (merged)
merged = pd.merge(df1,df3, on="Year", how = "left")
merged.set_index("Year", inplace=True)
print (merged)
merged = pd.merge(df1,df3, on="Year", how = "outer")
merged.set_index("Year", inplace=True)
print (merged)
merged = pd.merge(df1,df3, on="Year", how = "inner")
merged.set_index("Year", inplace=True)
print (merged)


