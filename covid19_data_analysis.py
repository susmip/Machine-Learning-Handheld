# -*- coding: utf-8 -*-
"""covid19 data analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TzcsRtTFbGg_qabLRxQcaMaVQHH5KTXZ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv('/content/covid19_Confirmed_dataset.csv')
dataset.head(5)

dataset.info()

"""**Delete useless column**"""

df=dataset.drop(['Lat','Long'],axis=1,inplace=True)
print(df)

print(dataset.head())

"""**aggregate rows by country**"""

corona_dataset_aggregated=dataset.groupby("Country/Region").sum()

print(corona_dataset_aggregated.head())

print(corona_dataset_aggregated.shape)

"""**visualize data related to a country**"""

corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['India'].plot()
corona_dataset_aggregated.loc['Germany'].plot()
plt.legend()

"""**calculate a good measure**"""

corona_dataset_aggregated.loc["China"][:3].plot()
plt.title("first three days")

"""**calculate the first derivative**"""

corona_dataset_aggregated.loc['China'].diff().plot()

"""**maximum infection**"""

corona_dataset_aggregated.loc["China"].diff().max()

countries=list(corona_dataset_aggregated.index)
max_infection_rates=[]
for c in countries:
  max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())

corona_dataset_aggregated['infection_Rates']=max_infection_rates

corona_dataset_aggregated.head()

corona_data=pd.DataFrame(corona_dataset_aggregated['infection_Rates'])

corona_data

#importing happiness dataset 2

happiness_report=pd.read_csv('/content/worldwide_happiness_report.csv')

happiness_report.head()

#dropping useless columns
useless_cols=["Overall rank","Score","Generosity","Perceptions of corruption"]

happiness_report.drop(useless_cols,axis=1,inplace=True)

print(happiness_report.head())

happiness_report.set_index("Country or region",inplace=True)

happiness_report.head()

"""**join data**"""

data=corona_data.join(happiness_report,how='inner')

data.corr()

"""**visualize data**"""

data.head()

x=data["GDP per capita"]
y=data["infection_Rates"]
sns.scatterplot(x,np.log(y)) #log scale

"""**regresssion plot**"""

sns.regplot(x,np.log(y))

"""**social support**"""

x=data["Social support"]
y=data["infection_Rates"]

sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

x=data["Healthy life expectancy"]
y=data["infection_Rates"]
sns.scatterplot(x,np.log(y))

x=data["Freedom to make life choices"]
y=data["infection_Rates"]
sns.scatterplot(x,np.log(y))