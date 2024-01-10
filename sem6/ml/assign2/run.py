import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('./Heart.csv')
# print(df.columns)
def display_dtypes_and_extract(df):
    x = df.dtypes.to_dict()
    extracted_cols = []
    for k, v in x.items():
        # print(f"{k} ==> {v}")
        print(f"{k} => {v}")
        if v == np.int64 or v == np.float64:
            extracted_cols.append(k)
    return extracted_cols

# we can ignore the first column which is the serial number, so we drop it
df = df.drop(['Unnamed: 0'], axis=1)

# code to display dtypes of each column and getting the float and int cols
print("The data types of all the columns:\n")
ext_cols = display_dtypes_and_extract(df)
print("\n[INFO] Integer and Float columns extracted")

# filtering the dataset to get only the columns containing float and int values
df_filtered = df.filter(ext_cols, axis=1)
df_filtered.to_csv('Heart_filtered.csv', index=False) # writing to a new CSV file
print("[INFO] Dataset filtered and written to file")

# identifying the missing values and filling them up with the median
print(f"[INFO] Missing values before filling with median: {df_filtered.isna().sum().sum()}")
df_filtered = df_filtered.fillna(df.mean(numeric_only=True))
print(f"[INFO] Missing values after filling with median: {df_filtered.isna().sum().sum()}")
df_filtered.to_csv('Heart_filtered.csv', index=False)

# converting to binary

