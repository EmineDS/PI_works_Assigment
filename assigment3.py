import pandas as pd
data=pd.read_excel(".\\assigment3.xlsx")
print("BEFORE SEPERATING *****************************************")
print(data)
data.Stats_Access_Link=data.Stats_Access_Link.str.split("\\").str[2]
data.Stats_Access_Link=data.Stats_Access_Link.str.split("<").str[0]
print("AFTER SEPERATING *******************************************")
print(data)