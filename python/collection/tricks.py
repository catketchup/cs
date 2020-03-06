## run bash scripts in python
result = subprocess.run(["bash", "/home/ketchup/tools/ANNZ/singleReg_quick.sh"], stdout=subprocess.PIPE)
result.stdout

## read in the files with same format
import glob
files = glob.glob(os.path.join(path, '*.npy')) # for a given directory
files = glob.glob('*.npy') # for the current directory
