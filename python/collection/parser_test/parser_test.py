import os, sys, time, stat
import math, random, string
import argparse

parser = argparse.ArgumentParser(description='Test parser')
parser.add_argument("N", type=int, help='Number of MPI jobs')
parser.add_argument("Command", type=str, help='Command')
parser.add_argument("-t", "--threads",     type=int,  default=1,help="Number of threads / cores to stride")

args = parser.parse_args()
N = args.N
Command = args.Command
t = args.threads

print(args)
print(N, Command, t)

# usage: python parser_test.py
# python parser_test.py 3 "test"
