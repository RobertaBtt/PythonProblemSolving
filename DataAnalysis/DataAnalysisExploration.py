import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

# Analyzing Individual Feature Patterns using Visualization

# How to choose the right visualization method?
# When visualizing individual variables, it is important to first
# understand what type of variable you are dealing with.
# This will help us find the right visualization method for that variable.

# list the data types for each column
print(df.dtypes)

# We can calculate the correlation between variables of type "int64" or "float64" using the method "corr"
df.corr()

# Find the correlation between the following columns: bore, stroke,compression-ratio , and horsepower.
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

# Continuous numerical variables:
# Positive linear relationship

# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)

# We can examine the correlation between 'engine-size' and 'price' and see it's approximately 0.87
df[["engine-size", "price"]].corr()

# Highway mpg is a potential predictor variable of price
sns.regplot(x="highway-mpg", y="price", data=df)

# As the highway-mpg goes up, the price goes down: this indicates an
# inverse/negative relationship between these two variables. Highway mpg could potentially be a predictor of price.
# We can examine the correlation between 'highway-mpg' and 'price' and see it's approximately -0.704

df[['highway-mpg', 'highway-mpg']].corr()

# Weak Linear Relationship
# Let's see if "Peak-rpm" as a predictor variable of "price".

sns.regplot(x="peak-rpm", y="price", data=df)

# Peak rpm does not seem like a good predictor of the price at all since the regression line is close to horizontal.
# We can examine the correlation between 'peak-rpm' and 'price' and see it's approximately -0.101616
df[['peak-rpm','price']].corr()

# Find the correlation between x="stroke", y="price".
df[["stroke","price"]].corr()

# Given the correlation results between "price" and "stroke" do you expect a linear relationship?
sns.regplot(x="stroke", y="price", data=df)

# Categorical variables
# These are variables that describe a 'characteristic' of a data unit, and are selected from a small group of categories.
# A  good way to visualize categorical variables is by using boxplots.
# Let's look at the relationship between "body-style" and "price".
sns.boxplot(x="body-style", y="price", data=df)

#  Let's examine engine "engine-location" and "price":
sns.boxplot(x="engine-location", y="price", data=df)

#  Let's examine "drive-wheels" and "price".
# drive-wheels
sns.boxplot(x="drive-wheels", y="price", data=df)

# 3. Descriptive Statistical Analysis
df.describe()

# The default setting of "describe" skips variables of type object.
# We can apply the method "describe" on the variables of type 'object' as follows:

df.describe(include=['object'])

# Value-counts is a good way of understanding how many units of each characteristic/variable we have
df['drive-wheels'].value_counts()


#We can convert the series to a Dataframe as follows:
df['drive-wheels'].value_counts().to_frame()

# Let's repeat the above steps
# but save the results to the dataframe "drive_wheels_counts" and rename the column 'drive-wheels' to 'value_counts'.

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts

# Now let's rename the index to 'drive-wheels':
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts

# We can repeat the above process for the variable 'engine-location'.
# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)


# 4. Basics of Grouping¶
#The "groupby" method groups data by different categories.
# The data is grouped based on one or several variables and analysis is performed on the individual groups.
#For example, let's group by the variable "drive-wheels". We see that there are 3 different categories of drive wheels.

df['drive-wheels'].unique()

#If we want to know, on average, which type of drive wheel is most valuable, we can group "drive-wheels" and then average them.
# We can select the columns 'drive-wheels', 'body-style' and 'price', then assign it to the variable "df_group_one".

df_group_one = df[['drive-wheels','body-style','price']]

# We can then calculate the average price for each of the different categories of data.
# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one

# You can also group with multiple variables. For example, let's group by both 'drive-wheels' and 'body-style'. This groups the dataframe
# by the unique combinations 'drive-wheels' and 'body-style'. We can store the results in the variable 'grouped_test1'.

# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1

# This grouped data is much easier to visualize when it is made into a pivot table.
# A pivot table is like an Excel spreadsheet, with one variable along the column and another along the row.
# We can convert the dataframe to a pivot table using the method "pivot " to create a pivot table from the groups.
# In this case, we will leave the drive-wheel variable as the rows of the table,
# and pivot body-style to become the columns of the table:
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')

# Often, we won't have data for some of the pivot cells. We can fill these missing cells with the value 0,
# but any other value could potentially # be used as well.
# It should be mentioned that missing data is quite a complex subject and is an entire course on its own.
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0

# Use the "groupby" function to find the average "price" of each car based on "body-style" ?
# grouping results
df_gptest2 = df[['body-style','price']]
grouped_test_bodystyle = df_gptest2.groupby(['body-style'],as_index= False).mean()
grouped_test_bodystyle


# Let's use a heat map to visualize the relationship between Body Style vs Price.

#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

# The default labels convey no useful information to us. Let's change that:

fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()

# 5. Correlation and Causation
# Correlation: a measure of the extent of interdependence between variables.
# Causation: the relationship between cause and effect between two variables.
# It is important to know the difference between these two and
# that correlation does not imply causation. Determining correlation is much simpler
# the determining causation as causation may require independent experimentation.

#Pearson Correlation is the default method of the function "corr".
# Like before we can calculate the Pearson Correlation of the of the 'int64' or 'float64' variables.
df.corr()

#P-value:
#
# What is this P-value? The P-value is the probability value that the correlation between these two variables
# is statistically significant. Normally, we choose
# a significance level of 0.05, which means that we are 95% confident that the correlation between the variables is significant.
# Wheel-base vs Price
# Let's calculate the Pearson Correlation Coefficient and P-value of 'wheel-base' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# Horsepower vs Price
# Let's calculate the Pearson Correlation Coefficient and P-value of 'horsepower' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Length vs Price
# Let's calculate the Pearson Correlation Coefficient and P-value of 'length' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)


# Width vs Price
# Let's calculate the Pearson Correlation Coefficient and P-value of 'width' and 'price':
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )

# Curb-weight vs Price
# Let's calculate the Pearson Correlation Coefficient and P-value of 'curb-weight' and 'price':
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Engine-size vs Price
# Let's calculate the Pearson Correlation Coefficient and P-value of 'engine-size' and 'price':
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)


# 6 . ANOVA
# ANOVA: Analysis of Variance
# The Analysis of Variance (ANOVA) is a statistical method used to test whether there are significant
# differences between the means of two or more groups.
# ANOVA returns two parameters:
# F-test score: ANOVA assumes the means of all groups are the same, calculates how much
# the actual means deviate from the assumption, and reports it as the F-test score.
# A larger score means there is a larger difference between the means.
# P-value: P-value tells how statistically significant is our calculated score value.


# #Drive Wheels
# Since ANOVA analyzes the difference between different groups of the same variable, the groupby function
# will come in handy. Because the ANOVA algorithm averages the data automatically, we do not need to take the average before hand.

grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)

df_gptest

grouped_test2.get_group('4wd')['price']

# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'],
                              grouped_test2.get_group('4wd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)

# Separately: fwd and rwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)

# 4 wd and rwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)

# 4 wd and fwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)
