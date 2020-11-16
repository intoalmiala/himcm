import csv, consts, random
import pandas as pd

with open(consts.PERSONPATH) as f:
    n = len(f.readlines()) - 1


tags = []
for _ in range(n):
    k = random.randrange(3, 5)
    tags.append(", ".join(random.sample(consts.TAGS, k)))

data = pd.read_csv("data/persondata.csv")
data["tags"] = tags


data.to_csv("data/persondata2.csv")
