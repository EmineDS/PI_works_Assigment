import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split,KFold
import sklearn.metrics as mt
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import sklearn.preprocessing as pr
from sklearn.linear_model import LogisticRegression,LogisticRegressionCV,LinearRegression
from sklearn.decomposition import PCA
pd.set_option('display.max_rows', None)  # Tüm satırları göster
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
data2=pd.read_csv(R"C:\Users\edisa\Downloads\dataset (2).csv")
data=data2.copy()

#manipuating to null cells
label=pr.LabelEncoder().fit_transform(data["isVirus"])
data["virus"]=label
data.drop(columns="isVirus",inplace=True)

data["feature_1"].fillna(data["feature_1"].mean(),inplace=True)
data["feature_2"].fillna(data["feature_2"].mean(),inplace=True)
data["feature_3"].fillna(data["feature_3"].mean(),inplace=True)
data["feature_4"].fillna(data["feature_4"].mean(),inplace=True)

Q3=data.feature_2.quantile(0.75)
Q1=data.feature_2.quantile(0.25)
IQR=Q3-Q1
top=Q3+1.5*IQR
bottom=Q1-1.5*IQR
data.loc[data["feature_2"] > top, "feature_2"] = top
data.loc[data["feature_2"] < bottom, "feature_2"] = bottom
Q3=data.feature_3.quantile(0.75)
Q1=data.feature_3.quantile(0.25)
IQR=Q3-Q1
top=Q3+1.5*IQR
bottom=Q1-1.5*IQR
data.loc[data["feature_3"] > top, "feature_3"] = top
data.loc[data["feature_3"] < bottom, "feature_3"] = bottom

sns.pairplot(data)
plt.title("no multicollinearity",size=35)
plt.show()

sns.boxplot(data)
plt.title("no outlier")
plt.show()
y=data["virus"]
print(data.isnull().sum())
X=data.drop(columns="virus",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=87)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)
pca=PCA()
X_train=pca.fit_transform(X_train)
X_test=pca.fit_transform(X_test)
#x train ve x testi temel bileşen yapısına ayırdık
lr_CV=LogisticRegressionCV(cv=4,random_state=42)
lr_CV.fit(X_train,y_train)
predict=lr_CV.predict(X_test)
r2=mt.r2_score(y_test,predict)
rmse=mt.mean_squared_error(y_test,predict,squared=True)
print(r2,rmse)
sns.heatmap(confusion_matrix(y_test,predict),annot=True)
plt.show()
#*********************************************************************************
# I CLEANED THE DATASET AND MANIPULATED THE DATA BUT EVEN IFI TRIED I COULD NOT INCRASE SCORE VALUE.
#IT COULD BE BETTER BUT I AM NOT ENOUGH FOR FIXING THAT PROBLEM TODAY. BUT IT MIGHT BE OVERFITTING
#I USED PCA OR CROSS VALIDATION FOR FIXING BUT I SHOULD BE MISSED SOMETHING
#IT WAS A FUN PROJECT. THANKS. I HAVE TO CHOOSE TO SEND EVEN IF THE PROJECT İS NOT COMPLETED
#AND I WILL FIND SOLUTION BY MYSELF
#*****************************************************************************************