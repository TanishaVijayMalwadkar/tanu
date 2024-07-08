import pandas as pd
s=pd.Series([1,3,5,7,9])
print(s)

data={'a':[1,2,3],'b':[4,5,6]}
df=pd.DataFrame(data)
print(df)

calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)

data={"cal":[420,380,390],"dur":[50,40,45]}
myvar1=pd.DataFrame(data)
print(myvar1)
#print(df.loc["day2"])