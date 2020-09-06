import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')


df_can.head()
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10)
df_can.tail()

df_can.info()
df_can.columns.values
df_can.index.values

print(type(df_can.columns))
print(type(df_can.index))

df_can.columns.tolist()
df_can.index.tolist()

print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))

# size of dataframe (rows, columns)
df_can.shape

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

df_can['Total'] = df_can.sum(axis=1)

df_can.isnull().sum()
df_can.describe()

#Example: Let's try filtering on the list of countries ('Country').

df_can.Country  # returns a series
#Let's try filtering on the list of countries ('OdName') and the data for years: 1980 - 1985.

df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers.
# for the sake of consistency, we will convert all column names to string later on

#Before we proceed, notice that the defaul index of the dataset is a numeric range from 0 to 194.
#This makes it very difficult to do a query by a specific country. For example to search for data on Japan,
#we need to know the corressponding index value.

#This can be fixed very easily by setting the 'Country' column as the index using set_index() method.

df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.head(3)

# optional: to remove the name of the index
df_can.index.name = None

#Example: Let's view the number of immigrants from Japan (row 87) for the following scenarios:' \
 #    1. The full row data (all columns) 2. For year 2013 3. For years 1980 to 1985

# 1. the full row data (all columns)
print(df_can.loc['Japan'])
# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())
# 2. for year 2013
print(df_can.loc['Japan', 2013])
#alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36
# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])
# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

#Column names that are integers (such as the years) might introduce some confusion.
#For example, when we are referencing the year 2013, one might confuse that when the 2013th positional index.
#To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.

df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

#Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years:

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years
# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

### Filtering based on a criteria


# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)
# 2. pass this condition into the dataFrame
df_can[condition]
# we can pass mutliple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

#note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

#Before we proceed: let's review the changes we have made to our dataframe.

print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)
print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)

# Matplot lib
# we are using the inline backend
#%matplotlib inline

print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0

# optional: apply a style to Matplotlib.
print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style

#Question: Plot a line graph of immigration from Haiti using df.plot().

#First, we will extract the data series for Haiti.

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()
haiti.plot()

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure

#########
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake.
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show()