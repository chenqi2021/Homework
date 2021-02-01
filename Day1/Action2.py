from pandas import Series, DataFrame
data = {'姓名':['张飞', '关羽', '刘备', '典韦', '许褚'],'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
print(data)
df1 = DataFrame(data)
# df1.set_index('姓名',inplace=True)
print(df1)
print(df1.describe())
print(df1.var())
df1["总分"] = df1.sum(axis=1)
df2 = df1.sort_values("总分", ascending=False)
print(df2)
