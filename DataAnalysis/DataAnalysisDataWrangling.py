import pandas as pd
import matplotlib.pylab as plt
import numpy as np

import matplotlib as plt
from matplotlib import pyplot

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)

# To see what the data set looks like, we'll use the head() method.
df.head()

#Identify missing values


# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

#Evaluating for missing data
# .isnull
# .notnull


missing_data = df.isnull()
missing_data.head(5)

# Count missing values in each column

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

# Deal with missing data

#Using Average
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# Using mean
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)

# Example with column stroke
avg_stroke=df['stroke'].astype('float').mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

# column horsepower
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)

#Replace NaN by mean
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

#MEan value for peak-rpm
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# To see which values are present in a particular column, we can use the ".value_counts()" method:
df['num-of-doors'].value_counts()

# idxmax()" method to calculate for us the most common type automatically:
df['num-of-doors'].value_counts().idxmax()

#replace the missing 'num-of-doors' values by the most frequent
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# Finally, let's drop all rows that do not have price data:
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

# Types for each column
df.dtypes

# Converta Data in the proper format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Data Standardization
# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# Highway-mpg
df["highway-mpg"] = 235/df["highway-mpg"]
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)
df.head()

#Data Normalization
# Would like to Normalize those variables so their value ranges from 0 to 1.
# Approach: replace original value by (original value)/(maximum value)

# replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()



# Write your code below and press Shift+Enter to execute
df['height'] = df['height']/df['height'].max()
df[["length","width","height"]].head()


# Binning
# Binning is a process of transforming continuous numerical variables into discrete categorical 'bins', for grouped analysis.

df["horsepower"]=df["horsepower"].astype(int, copy=True)

plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

# We would like 3 bins of equal size bandwidth so we use numpy's linspace(start_value, end_value, numbers_generated function.
# Since we want to include the minimum value of horsepower we want to set start_value=min(df["horsepower"]).
# Since we want to include the maximum value of horsepower we want to set end_value=max(df["horsepower"]).
# Since we are building 3 bins of equal length, there should be 4 dividers, so numbers_generated=4.

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins

# We set group names:
group_names = ['Low', 'Medium', 'High']

# We apply the function "cut" the determine what each value of "df['horsepower']" belongs to.

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

# Lets see the number of vehicles in each bin
df["horsepower-binned"].value_counts()

# Lets plot the distribution of each bin

pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# Bin visualizaion

a = (0,1,2)

# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# Indicator variable (or dummy variable)
# What is an indicator variable?
# An indicator variable (or dummy variable) is a numerical variable used to label categories.
# They are called 'dummies' because the numbers themselves don't have inherent meaning.
#
# Why we use indicator variables?
# So we can use categorical variables for regression analysis in the later modules.
#
# Example
# We see the column "fuel-type" has two unique values, "gas" or "diesel". Regression doesn't understand words, only numbers.
# To use this attribute in regression analysis, we convert "fuel-type" into indicator variables.
# We will use the panda's method 'get_dummies' to assign numerical values to different categories of fuel type.

df.columns

dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.head()

# Change column names for clarity
dummy_variable_1.rename(columns={'fuel-type-diesel':'gas', 'fuel-type-diesel':'diesel'}, inplace=True)
dummy_variable_1.head()

# We now have the value 0 to represent "gas" and 1 to represent "diesel"
# in the column "fuel-type". We will now insert this column back into our original dataset.

# merge data frame "df" and "dummy_variable_1"
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)

# Write your code below and press Shift+Enter to execute
dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
dummy_variable_2.head()


# Merge the new dataframe to the original dataframe then drop the column 'aspiration'
# Write your code below and press Shift+Enter to execute
df = pd.concat([df, dummy_variable_2], axis=1)
df.drop('aspiration', axis = 1, inplace=True)

# Save thenew CSV
df.to_csv('clean_df.csv')
