from mpi4py import MPI
import sys
import time

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

sys.stdout.write("Hello, World! I am process %d of %d on %s.\n" %
                 (rank, size, name))
time.sleep(300)

from mpi4py import MPI
import numpy as np
from orphics import stats
# example: https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_split.html
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# x = np.arange(7.0)
# list = np.array_split(x, 4)
# print(list)
# print("my rank is %d:" % rank)
# for i in list[rank]:
#     print(i)


def fun_mpi(rank):
    x = np.arange(7.0)
    list = np.array_split(x, 4)
    print("my rank is %d:" % rank)
    st = stats.Stats()

    for i in list[rank]:
        data = [rank, rank]
        st.add_to_stats('index', data)

    st.get_stats()


fun_mpi(rank)
© 2020 GitHub, Inc.
