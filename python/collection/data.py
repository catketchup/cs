import panda as pd
import numpy as np

## read in data, converted it to csv and array, use pd.DataFrame to process it (load catalog data)
def load_data(cat_filename):
    """Loads a given number of rows from catalog and return test and train"""
    # load catalog data, convert the data in to a function so that we can process it
    cat_data = pd.read_csv(cat_filename,
                        delim_whitespace=True,
                        comment='#',
                        header=None)
    # give column names
    cat_data.columns = ['id','redshift','tu','tg','tr','ti','tz','ty',\
                        'u10','uerr10','g10','gerr10','r10','rerr10',\
                        'i10','ierr10','z10','zerr10','y10','yerr10']

    return cat_data

## export csv data
df=pd.DataFrame(X_train) #transfer the numpy.array to DataFrame format
df.to_csv("path/filename.csv", index=False, header=False)

## check a certain column
df['column_name']
df['column_name'].plot()
df['column_name'].hist()

## cut the head or tail rows as new catalog data
df.head(n=5)
df.tail(n=5)




## save numpy.array data 
import os
# read in csv file
eval_path = '/home/ketchup/tools/ANNZ/output/test_singleReg_quick/regres/eval/'
eval_file = eval_path + 'ANNZ_singleReg_0000.csv'
cat_data = pd.read_csv(eval_file, comment='#', header=None) # cat_data is pd.DataFrame data

data = np.array(cat_data) # convert it into numpy.array
output_dir = '/home/ketchup/tools/ANNZ/scripts/sizes/'
output_file = 'test.npy'

np.save(output_file, data) # save to current directory
np.save(os.path.join(output_dir, output_file), data) # save to a certain directory
np.save(output_dir + output_file, data) # save to a certain directory

## load in npy data
data = np.load(output_dir + 'test.npy') # now data is a numpy.array


## load in all npy files
files = glob.glob(path + '*.npy')