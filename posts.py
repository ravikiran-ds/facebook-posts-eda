# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:23:46 2020

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing
df=pd.read_csv('data.txt',sep='/t')

#exploring data
df.head()
df.tail()
df.info()
df.describe()
df.dtypes

#getting freatures
df['date']=df.date.apply(lambda x:x.replace(',',''))
df['date']=pd.to_datetime(df.date)
df['year']=df.date.dt.year
df['month']=df.date.dt.month
df['day']=df.date.dt.day
df['hour']=df.date.dt.hour

#bar plot
def bar_plt(df,col_name,title=None,xlabel=None,ylabel=None,ascending=True,start=None,stop=None):
    df[col_name].value_counts().sort_values(ascending=ascending)[start:stop].plot.bar()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


#EDA
#2018 is dominating
bar_plt(df,"year",title="Year By year",xlabel="Year",ylabel="No of Posts")
#removing 2018 to see other years
bar_plt(df,"year",title="Year By year",xlabel="Year",ylabel="No of Posts",start=0,stop=-1)
#january Donimates
bar_plt(df,"month",title="Month by Month",xlabel="Month",ylabel="No of Posts")
#removing january to look at other months
bar_plt(df,"month",title="Month by Month",xlabel="Month",ylabel="No of Posts",start=0,stop=-1)
#10 am and 8pm most common
bar_plt(df,"hour",title="Hour by Hour",xlabel="Hour",ylabel="No of Posts")
#removing 10am and 8pm
bar_plt(df,"hour",title="Hour by Hour",xlabel="Hour",ylabel="No of Posts",start=0,stop=-2)

#in the morning posts
df.loc[df['hour']<12,'hour'].value_counts().plot.bar()
plt.title("In the morning")
plt.xlabel("TIme in hrs")
plt.ylabel("no of posts")
plt.show()
#evening posts
df.loc[df['hour']>12,'hour'].value_counts().plot.bar()
plt.title("In the evening")
plt.xlabel("TIme in hrs")
plt.ylabel("no of posts")
plt.show()


#2018 dominates
df.groupby('year')['month'].value_counts().plot.line()
plt.xticks(rotation='vertical')
plt.title("Year and month")
plt.xlabel("Year and Month")
plt.ylabel("No of posts")
plt.show()

#removing 2018
df.groupby('year')['month'].value_counts()[0:-1].plot.line()
plt.xticks(rotation='vertical')
plt.title("Year and month")
plt.xlabel("Year and Month")
plt.ylabel("No of posts")
plt.show()