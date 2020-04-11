# Implement simple MinHash generator
from sklearn.utils import murmurhash3_32
import random
random.seed(24)


def hashfunc_gen():
    rand_seed = random.randint(0, 2^24)
    return lambda x: murmurhash3_32(x, seed=rand_seed)


def hashcodes_gen(string, m):
    hashcodes = []
    for i in range(m):
        hashcodes.append(hashfunc_gen()(m))
    return hashcodes

print(hashcodes_gen("aids", 100))




# Import dataset
# import csv
# import pandas as pd
# data = pd.read_csv("../user-ct-test-collection-01.txt", sep="\t")
# urllist = data.ClickURL.dropna().unique()
# print(urllist)
# print(2**24)
