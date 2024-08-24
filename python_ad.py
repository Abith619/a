import numpy as np
import pandas as pd
import platform

df2 =pd.read_csv('task2.csv')
arr5 = df2["emp salary"].values
data1  = np.random.randint(100, size = arr5.shape)

combined_array = np.vstack((arr5, data1))
variance_per_column = np.var(combined_array, axis=1)
variance_per_row = np.var(combined_array, axis=0)
# combined_array = np.concatenate((arr5,data1))
# data3 = np.var(combined_array)

print("Variance per column:", variance_per_column)
print("Variance per row:", variance_per_row)

# data1 = np.random.randint(1, 100, size=(1, 15))

# var_arr5 = np.var(arr5)
# var_data1 = np.var(data1)

# print(f"Variance of arr5: {var_arr5}")
# print(f"Variance of data1: {var_data1}")


