import pandas as pd
import json

# def gbk2UTF(line):
#     try:
#         line = line.decode("gbk").encode("utf-8")
#     except:
#         return line
#     else:
#         return line


data = pd.read_csv(r'price2016.csv',encoding="gbk")
dictionary = dict()
li = list(data.columns)
for i in range(len(li)):
    dictionary[li[i]] = list(data.loc[::][list(data.columns)[i]])
print(json.dumps(dictionary))


