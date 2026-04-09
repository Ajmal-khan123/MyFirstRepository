import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### The preprocessing stage of the data set

dt=pd.read_csv('selection.csv')
print("The whole record in the computer  visualization of the data=>",dt)

#the head of the data
# print(dt.head(10))

#shape of the data set
# print(dt.shape)


#Remove the first col which show the serial number
dis=dt.iloc[:,1:]
# print(dis)

#find the null value in the data set
nul=dt.isnull()
# print("the null value",nul)

#find the median of the iq
Aq=dt['iq'].median()
# print("The median of the IQ=",Aq)

#find the mean of the of data
AMe=dt['iq'].mean()
# print("The mean of the data",AMe)


#Find the mode of the data
AMo=dt['iq'].mode()
# print("The mode of the data=",AMo)

#find the max of the iq
AMX=dt['iq'].max()
# print("The maximum =",AMX)

#find the min of the iq
AMN=dt['iq'].min()
# print("The minimum =",AMN)

#__2__ step! EDA  (Exploratory of the data)
#Now we will plot the data between iq and cgpa

#_____________X-axis,___Y-axis
# pl=dt.plt.scatter(dt['cgpa'],dt['iq'])
# print("To visualize the data",pl)
# dt['placement'] = dt['placement'].map({'yes': 1, 'no': 0})
# vis = dt.plot.scatter(x='cgpa', y='iq', cmap='coolwarm', c=dt['placement'])
vis=dt.plot.scatter(x='cgpa', y='iq',  c=dt['placement'])
plt.show()
plt.title("Comparison based selection __maintain__ is must")
plt.xlabel("CGPA")
plt.ylabel("IQ")
print(vis)

from sklearn.model_selection import train_test_split