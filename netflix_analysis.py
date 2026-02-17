import pandas as pd

data = pd.read_csv("netflix.csv")

print("Netflix Dataset:")
print(data)

print("\nFirst 5 Rows:")
print(data.head())

print("\nCount of Movies and TV Shows:")
print(data["Type"].value_counts())

print("\nMost Common Genre:")
print(data["Genre"].value_counts())

movies = data[data["Type"] == "Movie"]
print("\nMovies Only:")
print(movies)

recent = data[data["Release_Year"] > 2018]
print("\nRecent Shows:")
print(recent)

print("\nContent by Country:")
print(data["Country"].value_counts())

oldest = data[data["Release_Year"] == data["Release_Year"].min()]
print("\nOldest Show:")
print(oldest)