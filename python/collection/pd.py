import numpy as np
import pandas as pd

# create two numpy array
np_x = np.arange(1, 6, 1)
np_y = np.arange(1, 10, 2)
print(np_x)
print(np_y)

# create a dict using ny_x and np_y
np_data = {'x': np_x, 'y': np_y}

# 1.
# define index_1, a list
index_1 = ['a', 'b', 'c', 'd', 'e']
# define index_2, a numpy array
index_2 = np_x

# add np_x and np_y into a DataFrame with index
df_data_1 = pd.DataFrame(np_data, index=index_2)
print('df_data_1')
print(df_data_1)

# 2.
df_data_2 = pd.DataFrame(np_data)
df_data_2.index = index_2
print('df_data_2')
print(df_data_2)

# export data
df_data_1.to_csv('output/df_data.dat', index=False)

# import data by pd.read_csv
ip_df_data = pd.read_csv('output/df_data.dat')
print('import data by read_csv')
print(ip_df_data)

# show column of 'x'
col_1 = ip_df_data['x']
print(col_1)
# convert it into a np.array
col_1 = np.array(col_1)
print(col_1)
