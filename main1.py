import plotly.express as px
import csv 
Coffee=[]
sleep=[]
with open("data2.csv") as f:
    df=csv.DictReader(f)
    for row in df:
        Coffee.append(float(row["Coffee"]))
        sleep.append(float(row["sleep"]))
import numpy as np
cor=np.corrcoef(Coffee,sleep)
print(cor[0,1])
  