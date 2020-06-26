from mpi4py import MPI
import numpy as np
from orphics import stats
# example: https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_split.html
# use mpirun -n 4 python MPI_loop.py
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data_path = 'output/'

x = np.arange(7.0)

list = np.array_split(x, 4)
print(list)
print("my rank is %d:" % rank)

data = np.array([])
for i in list[rank]:
    print(i)
    data = np.append(data, i)
print(data)
print(type(data))
np.savetxt(data_path+f'rank{rank}.txt',data)
