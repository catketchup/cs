#!/bin/sh

#SBATCH --qos=debug
#SBATCH --time=5
#SBATCH --nodes=2
#SBATCH --tasks-per-node=2
#SBATCH --constraint=haswell

srun -n helloworld.py
