# Copy a column from one DataFrame to another in Pandas

import pandas as pd

df1 = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'profit': [1500, 2500, 3500, 4500],
})

df2 = pd.DataFrame({
    'employees': [10, 15, 20, 25],
})


df2['year'] = df1['year']
df2['profit'] = df1['profit']

#    employees  year  profit
# 0         10  2020    1500
# 1         15  2021    2500
# 2         20  2022    3500
# 3         25  2023    4500
print(df2)