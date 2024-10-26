"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

# Getting my CSV data
fname = "ellerun.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)
print("var names =", var_names)

# Extracting relevant data from the dataframe
problem_sizes = df[var_names[0]].values.tolist()
direct_sum_time = df[var_names[1]].values.tolist()
vector_sum_time = df[var_names[2]].values.tolist()
indirect_sum_time = df[var_names[3]].values.tolist()

# Constants
OPS_BASELINE = 1e6 
MEM_CAPACITY = 204.8 * 1024 * 1024 * 1024  # Peak memory bandwidth in bytes/s

# Lists for MFLOPS, memory bandwidth, and memory latency
mflops_direct, mflops_vector, mflops_indirect = [], [], []
mem_bw_direct, mem_bw_vector, mem_bw_indirect = [], [], []
latency_direct, latency_vector, latency_indirect = [], [], []

# MFLOPS calculation
for size, t1, t2, t3 in zip(problem_sizes, direct_sum_time, vector_sum_time, indirect_sum_time):
    mflops_direct.append((2 * size / OPS_BASELINE) / t1)
    mflops_vector.append((3 * size / OPS_BASELINE) / t2)
    mflops_indirect.append((4 * size / OPS_BASELINE) / t3)

# Memory Bandwidth calculation
for size, t1, t2, t3 in zip(problem_sizes, direct_sum_time, vector_sum_time, indirect_sum_time):
    mem_bw_direct.append((size * 4 / t1) / MEM_CAPACITY * 100)  # Convert to percentage
    mem_bw_vector.append((size * 2 * 4 / t2) / MEM_CAPACITY * 100)  # Convert to percentage
    mem_bw_indirect.append((size * 3 * 4 / t3) / MEM_CAPACITY * 100)  # Convert to percentage

# Memory Latency calculation
for size, t1, t2, t3 in zip(problem_sizes, direct_sum_time, vector_sum_time, indirect_sum_time):
    latency_direct.append(t1 / size)
    latency_vector.append(t2 / (2 * size))
    latency_indirect.append(t3 / (3 * size))

# x-axis positions and labels
x_positions = list(range(len(problem_sizes)))
labels = [var_names[1], var_names[2], var_names[3]]

# Plot MFLOPS
plt.figure(figsize=(10, 6))
plt.plot(x_positions, mflops_direct, "r-o", label=labels[0])
plt.plot(x_positions, mflops_vector, "b-x", label=labels[1])
plt.plot(x_positions, mflops_indirect, "g-^", label=labels[2])
plt.xticks(x_positions, problem_sizes)
plt.title("MFLOP/s Comparison for Direct, Vector, and Indirect Sum")
plt.xlabel("Problem Sizes")
plt.ylabel("MFLOP/s")
plt.legend(loc="best")
plt.grid(True)
plt.show()

# Plot Memory Bandwidth
plt.figure(figsize=(10, 6))
plt.plot(x_positions, mem_bw_direct, "r-o", label=labels[0])
plt.plot(x_positions, mem_bw_vector, "b-x", label=labels[1])
plt.plot(x_positions, mem_bw_indirect, "g-^", label=labels[2])
plt.xticks(x_positions, problem_sizes)
plt.title("Memory Bandwidth Comparison for Direct, Vector, and Indirect Sum")
plt.xlabel("Problem Sizes")
plt.ylabel("Memory Bandwidth Utilization (%)")
plt.legend(loc="best")
plt.grid(True)
plt.show()

# Plot Memory Latency
plt.figure(figsize=(10, 6))
plt.plot(x_positions, latency_direct, "r-o", label=labels[0])
plt.plot(x_positions, latency_vector, "b-x", label=labels[1])
plt.plot(x_positions, latency_indirect, "g-^", label=labels[2])
plt.xticks(x_positions, problem_sizes)
plt.title("Memory Latency Comparison for Direct, Vector, and Indirect Sum")
plt.xlabel("Problem Sizes")
plt.ylabel("Memory Latency")
plt.legend(loc="best")
plt.grid(True)
plt.show()

# EOF
