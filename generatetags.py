import csv, consts, random

with open(consts.PERSONPATH) as f:
    n = len(f.readlines()) - 1

with open("persontags.csv", "w") as f:
    for _ in range(n):
        k = random.randrange(1, len(consts.TAGS)+1)
        tags = random.sample(consts.TAGS, k)
        f.write(", ".join(tags) + "\n")
