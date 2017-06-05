import pandas as pd  # to read data as dataframe
import matplotlib.pyplot as mp  # to plot
from matplotlib import pyplot as plt
import seaborn as sn



# to read data
data = pd.read_table("Data.txt")
# print(f.read())
print(type(data))
# df = pandas.DataFrame(f_list)
print(data.shape)
print(data.head(2))
data['K'] = data.sum(axis=1)
#print(data["Case-Control"])
sn.set_style("whitegrid")
sn.boxplot(x= "Case-Control",y="K",data= data )
sn.stripplot(x= "Case-Control",y="K",data= data,size=6, jitter=True, edgecolor="gray", split=True,linewidth=1)
sn.plt.suptitle('Boxplot with dots')
plt.subplots_adjust(top=0.92)
plt.ylabel('Total of amount')
plt.show()

sn.swarmplot(x= "Case-Control",y="K",hue= 'Gender', data= data )
sn.plt.suptitle('Plot by grouping categorical values')
plt.subplots_adjust(top=0.9)
plt.ylabel('Total of amount')
plt.show()

sn.lmplot(x= "A",y="K",hue= "Gender", data= data)
sn.plt.suptitle('Plot with linear \n regression plus \ncategorical coloured values', size= 15, horizontalalignment='center')
plt.subplots_adjust(top=0.85, right= 0.85)
plt.ylabel('Total of amount')
plt.xlabel('The first value')
plt.show()

