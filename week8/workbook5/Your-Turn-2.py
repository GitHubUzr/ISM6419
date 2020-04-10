def columnValues(col):
    x = []
    x.append(df[col].count())
    x.append(df[col].mean())
    x.append(round(df[col].std(),2))
    x.append(df[col].min())
    x.append(df[col].max())
    x.append(df[col].quantile(.25))
    x.append(df[col].quantile(.5))
    x.append(df[col].quantile(.75))
    x.append(df[col].median())
    if len(df[col].mode()) == len (df):
        x.append("all numbers")
    else:
        y = df[col].mode()
        x.append(str(y[0]))
    x.append(df[col].var())
    return x
    
import pandas as pd

# create a dataframe and compute summary statistics
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
MyList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=MyList,columns=['Names','Grades','BS Degrees','MS Degrees','PhD Degrees'])   
    
g = columnValues("Grades")
b = columnValues("BS Degrees")
m = columnValues("MS Degrees")
p = columnValues("PhD Degrees")
              
titles = ["Number of values","Arithmetic average","Standard deviation",
"Minimum","Maximum","First quartile","Second quartile","Third quartile","Median","Mode","Variance"]
MyList = zip(g,b,m,p)
df = pd.DataFrame(data=MyList,index=titles,columns = ['Grades','BS Degrees','MS Degrees','PhD Degrees'])
df

# alt method
# but all values are float
# a = []
# a.append(tuple(df.iloc[:, [1,2,3,4]].count()))
# a.append(tuple(df.mean()))
# a.append(tuple(df.std()))
# a.append(tuple(df.iloc[:, [1,2,3,4]].min()))
# a.append(tuple(df.iloc[:, [1,2,3,4]].max()))
# a.append(tuple(df.quantile(.25)))
# a.append(tuple(df.quantile(.5)))
# a.append(tuple(df.quantile(.75)))
# a.append(tuple(df.median()))
# temp = df.iloc[:, [1,2,3,4]].mode()
# a.append(tuple(temp.iloc[0]))
# a.append(tuple(df.var()))
# df = pd.DataFrame(data=a,columns=['Grades','BS','MS','PhD'])
# df