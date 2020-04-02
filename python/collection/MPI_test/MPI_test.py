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
