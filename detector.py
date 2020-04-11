import time

start_time = time.time()

# Task 0 1.
# Implement simple MinHash generator
from sklearn.utils import murmurhash3_32


def hashfunc_gen(i):
    return lambda x: murmurhash3_32(x, seed=i)


def trigrams(string):
    n = len(string)
    if n < 3:
        return set([])
    else:
        trigrams = []
        for i in range(n - 2):
            trigrams.append(string[i:i + 3])
        # print(trigrams)
        return set(trigrams)


def hashcodes_gen(string, m):
    hashcodes = []
    string_trigrams = trigrams(string)
    for i in range(m):
        hashfunc = hashfunc_gen(i)
        minval = float("inf")
        for trigram in string_trigrams:
            val = hashfunc(trigram)
            if val < minval:
                minval = val
                mintri = trigram
        hashcodes.append(mintri)
    return hashcodes


# print(hashcodes_gen("This is a test string. I hope this works?", 100))

# Task 0 2.
s1 = "The mission statement of the WCSCC and area employers recognize the importance of good \
attendance on the job. Any student whose absences exceed 18 days is jeopardizing their opportunity for \
advanced placement as well as hindering his/her likelihood for successfully completing their program."
s2 = "The WCSCC's mission statement and surrounding employers recognize the importance of great \
attendance. Any student who is absent more than 18 days will loose the opportunity for successfully \
completing their trade program."
hash_s1 = hashcodes_gen(s1, 100)
hash_s2 = hashcodes_gen(s2, 100)

# Estimate
equal = 0
for i in range(100):
    if hash_s1[i] == hash_s2[i]:
        equal += 1
print(equal / 100.0)
# Actual
print(len(set.intersection(trigrams(s1), trigrams(s2))) * 1.0 / len(set.union(trigrams(s1), trigrams(s2))))

# Task 0 3.
from collections import defaultdict


class HashTable():
    def __init__(self, k, l, r):
        self.k = k
        self.l = l
        self.r = r
        self.hashtables = [defaultdict(list)] * l
        self.l_hashfuncs = []
        self.kl_hashfuncs = []
        for i in range(l):
            self.l_hashfuncs.append(lambda x: murmurhash3_32(x, seed=i * 2 ** 24) % r)
            k_hashfuncs = []
            for j in range(k):
                k_hashfuncs.append(hashfunc_gen(i * k + j))
            self.kl_hashfuncs.append(k_hashfuncs)

    def insert(self, hashcodes, id):
        for i in range(self.l):
            self.hashtables[i][self.l_hashfuncs[i]("".join(hashcodes[i * self.k: (i + 1) * self.k]))].append(id)

    def lookup(self, hashcodes):
        solution = []
        for i in range(self.l):
            solution.extend(self.hashtables[i][self.l_hashfuncs[i]("".join(hashcodes[i * self.k: (i + 1) * self.k]))])
        return set(solution)

# Import dataset
import csv
import pandas as pd

data = pd.read_csv("../user-ct-test-collection-01.txt", sep="\t")
urllist = data.ClickURL.dropna().unique()[0:30000]

k = 2
l = 50
r = 20

hash_table = HashTable(k, l, r)
id_dict = {}
for i in range(len(urllist)):
    url = urllist[i]
    id_dict[url] = i
    hash_table.insert(hashcodes_gen(url, k * l), i)

# print(hash_table.hashtables[0][18])
# print(hash_table.hashtables[0][19])

print("--- %s seconds ---" % (time.time() - start_time))

# import random
# random.seed(24)
