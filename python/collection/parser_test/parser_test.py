import os, sys, time, stat
import math, random, string
import argparse

parser = argparse.ArgumentParser(description='Test parser')
parser.add_argument("N", type=int, help='Number of MPI jobs')
parser.add_argument("Command", type=str, help='Command')
args = parser.parse_args()
N = args.N
Command = args.Command
print(N, Command)
# usage: python parser_test.py
# python parser_test.py 3 "test"
