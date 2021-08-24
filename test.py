import pandas

c = [1,3]
dftest = pandas.DataFrame(columns = ['A','B'])
print(dftest)
series = pandas.Series(c, index = dftest.columns)
dftest = dftest.append(series, ignore_index= True)
print(dftest)