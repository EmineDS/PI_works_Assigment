#**********QUESTIONS 4 -5 **********************************************************************************************
#why we have to fill with 0? I filled null cells with min daily vaccination number and it is 1.
import pandas as pd
data=pd.read_csv(".\countryvac.csv")
pd.set_option('display.max_columns', None)
#print(data.isnull().sum())
minvacation=data.daily_vaccinations.min()
print("*****QUESTIONS 4 -5 **************")
print(minvacation)
data.daily_vaccinations.fillna(minvacation,inplace=True)
#**********QUESTIONS 6 **********************************************************************************************
means=data.groupby("country").daily_vaccinations.mean()
means=pd.DataFrame(means)
print("*****QUESTION 6 *****************")
print(means.nlargest(3,"daily_vaccinations"))
#**********QUESTIONS 7 **********************************************************************************************
date=data[data["date"]=="1/6/2021"]
print("*****QUESTION 7 *****************")
print(date.daily_vaccinations.sum())