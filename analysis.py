import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


RANKINGS = "data/rankings.csv"
JOBLIST = "data/jobslistfinal.csv"
PERSONLIST = "data/persondata.csv"

data = pd.read_csv(RANKINGS, delimiter=";", index_col="id")
people = pd.read_csv(PERSONLIST, index_col="Name")
jobs = pd.read_csv(JOBLIST, delimiter=";", na_values="None")
jobs["Score"] = np.zeros(272)

best = pd.DataFrame(data[["S0", "0"]], columns=["S0", "0"])
d = pd.merge(jobs, best, left_on="Id", right_on="S0").value_counts("Job title")

print(d)


# plt.xticks(rotation=-80, ha="left")
# plt.ylabel("Frequency")
# plt.xlabel("Job title")
# plt.title("Most recommended jobs by our algorithm")
# plt.plot(d)
# plt.tight_layout()
# plt.savefig("most_recommended.png")

scores = pd.Series(jobs["Score"]).astype(int)

for i in range(0, 272):
    # multiplier = 20/2**(i+1)
    multiplier = 16/(i+1)**2
    d1 = data[f"S{i}"]
    job = d1.value_counts() * multiplier
    scores = scores.add(job, fill_value=0, axis="index")
scores = scores.drop(0)
scores.index -= 1
print(scores)


lat = jobs["PosX"].astype(float)
lon = jobs["PosY"].astype(float)
plat = people["lat"].astype(float)
plon = people["lon"].astype(float)

plt.xticks([lon.min(), lon.max()])
plt.yticks([lat.min(), lat.max()])
# plt.scatter(lon, lat, s=scores)

plt.scatter(plon, plat, s=6, c="r", marker="s")

plt.show()

sorted_jobs = pd.concat((jobs["Job title"].rename("Title"), scores.rename("Score")), axis=1)
# sorted_jobs = sorted_jobs.set_index("Title")
sorted_jobs = sorted_jobs.groupby("Title").mean()
# sorted_jobs = sorted_jobs.groupby("Title").sum()
sorted_jobs = sorted_jobs.sort_values("Score", axis=0)

plt.xticks(rotation=-80, ha="left")

plt.bar(sorted_jobs.index, sorted_jobs["Score"])

plt.tight_layout()
plt.show()

somedata = data[["271"]].sort_values("271", axis=0)
print(somedata)