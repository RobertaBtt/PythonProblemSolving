import pandas as pd


other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)

print("The first 5 rows of the dataframe")
df.head(5)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)


df.columns = headers
df.head(10)

#Drop missing values
df.dropna(subset=["price"], axis=0)

#Print columnns
print(df.columns)

#Save Dataset
df.to_csv("automobile.csv", index=False)

# Info on Data Types
df.dtypes


# check the data type of data frame "df" by .dtypes
print(df.dtypes)

df.describe()

# describe all the columns in "df"
df.describe(include = "all")

columns_to_describe = ['length', 'compression-ratio']
df[columns_to_describe].describe()

#Info

df.info

