import pandas as pd

df = pd.read_csv("books.csv")

df.columns = df.columns.str.strip().str.lower()

print("Column names:", df.columns.tolist())

print("Column names:", [repr(col) for col in df.columns])

df.columns = df.columns.str.strip()

print("After removing spaces:", [repr(col) for col in df.columns])

print("CSV file location:", df.columns.tolist())

print("Dataset shape:", df.shape)

print("\nDuplicate rows:", df.duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)



# Convert price from text to numbers
df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(r"[^0-9.]", "", regex=True)
    .astype(float)
)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].str.strip().map(rating_map)
print("Original ratings:", df["rating"].unique())

# Convert rating from text to numbers
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")




# Basic analysis
print("\nTotal books:", len(df))

print("Average book price:", round(df["price"].mean(), 2))
print("Cheapest book price:", df["price"].min())
print("Most expensive book price:", df["price"].max())
print("Average book rating:", round(df["rating"].mean(), 2))

# Find the five most expensive books
print("\nTop 5 most expensive books:")

print(
    df[["title", "price"]]
    .sort_values(by="price", ascending=False)
    .head(5)
)

# Find the five highest-rated books
print("\nTop 5 highest-rated books:")

print(
    df[["title", "rating"]]
    .sort_values(by="rating", ascending=False)
    .head(5)
)

# Save cleaned data to a new CSV file
df.to_csv("books_cleaned.csv", index=False)

print("\nCleaned data saved to books_cleaned.csv")