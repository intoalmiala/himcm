import pandas as pd

COORDS = "jobcoordsoutput.csv"
OTHERDATA = "data/jobdatanew.csv"

coords = pd.read_csv(COORDS, delimiter=";", na_values="None")

data = pd.read_csv(OTHERDATA, delimiter=",")

data = data.loc[data.index.repeat(data["Frequency"])].assign(fifo_qty=1).reset_index(drop=True)
data = data.rename({"Lat": "PosX", "Lon": "PosY"}, axis=1)
data = data.drop(["Frequency"],axis=1)

newdata = pd.concat((data, coords), axis=1)
newdata["Id"] = range(1, len(newdata) + 1)
newdata = newdata[["Job title", "Id", *list(filter(lambda x: x not in ["Job title", "Id"], newdata.columns.values))]]
# print(newdata)
newdata.to_csv("jobslistfinal.csv", index=False)