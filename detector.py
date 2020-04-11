# import csv
# why doesn't it change
import pandas as pd
data = pd.read_csv("../user-ct-test-collection-01.txt", sep="\t")
querylist = data.Query.dropna()[data.Query.dropna() != "-"]
print(querylist.head())

