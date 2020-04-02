from mpi4py import MPI
# import sys
# import time

# # To study how to use python MPI
# size = MPI.COMM_WORLD.Get_size()

# rank = MPI.COMM_WORLD.Get_rank()
# name = MPI.Get_processor_name()

# sys.stdout.write("Hello, World! I am process %d of %d on %s.\n" %
#                  (rank, size, name))
# time.sleep(300)

# https://blog.csdn.net/qq_28081453/article/details/88982406
print("my rank is: %d" % MPI.COMM_WORLD.Get_rank())
# the same code will run on different processes
# usage: $ mpiexec -n 4 python helloworld.py
