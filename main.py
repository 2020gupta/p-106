import plotly.express as px
import csv 
RollNo=[]
Marks =[]
with open("data1.csv") as f:
    df=csv.DictReader(f)
    for row in df:
        RollNo.append(float(row["Roll No"]))
        Marks.append(float(row["Marks In Percentage"]))
import numpy as np
cor=np.corrcoef(RollNo,Marks)
print(cor[0,1])