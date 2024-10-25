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


fname = "ellerun.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

# Code 1: Direct Sum, Code 2: Vector Sum, Code 3: Indirect Sum
# Mflops code:
code1_mflops = []
code2_mflops = []
code3_mflops = []

for x in problem_sizes:
    for y in code1_time:
        code1_mflops.append((2*x/1000000)/y)

for x in problem_sizes:
    for y in code2_time:
        code2_mflops.append((3*x/1000000)/y)

for x in problem_sizes:
    for y in code3_time:
        code3_mflops.append((4*x/1000000)/y)

# Memory Bandwidth code:
code1_mem_bw = []
code2_mem_bw = []
code3_mem_bw = []

capacity = 204.8 * 1024 * 1024 * 1024
for x in problem_sizes:
    for y in code1_time:
        code1_mem_bw.append((x*4/y)/(capacity))

for x in problem_sizes:
    for y in code2_time:
        code2_mem_bw.append((x*2*4/y)/(capacity))

for x in problem_sizes:
    for y in code3_time:
        code3_mem_bw.append((x*3*4/y)/(capacity))

# Memory Latency code:
code1_mem_latency = []
code2_mem_latency = []
code3_mem_latency = []

for x in problem_sizes:
    for y in code1_time:
        code1_mem_latency.append(y/x)

for x in problem_sizes:
    for y in code2_time:
        code2_mem_latency.append(y/(2*x))

for x in problem_sizes:
    for y in code3_time:
        code3_mem_latency.append(y/(3*x))

# Customize x-axis ticks
xlocs = [i for i in range(len(problem_sizes))]

# Define legend labels
varNames = [var_names[1], var_names[2], var_names[3]]

# Plot for MFLOPS
plt.figure(figsize=(10, 6))
plt.title("Comparison of 3 Codes (MFLOPS)")
plt.plot(xlocs, code1_mflops, "r-o")
plt.plot(xlocs, code2_mflops, "b-x")
plt.plot(xlocs, code3_mflops, "g-^")
plt.xticks(xlocs, problem_sizes)
plt.xlabel("Problem Sizes")
plt.ylabel("MFLOPS")
plt.legend(varNames, loc="best")  # Add legend
plt.grid(axis='both')  # Enable grid lines
plt.show()

# Plot for Memory Bandwidth
plt.figure(figsize=(10, 6))
plt.title("Comparison of 3 Codes (Memory Bandwidth)")
plt.plot(xlocs, code1_mem_bw, "r-o")
plt.plot(xlocs, code2_mem_bw, "b-x")
plt.plot(xlocs, code3_mem_bw, "g-^")
plt.xticks(xlocs, problem_sizes)
plt.xlabel("Problem Sizes")
plt.ylabel("Memory Bandwidth")
plt.legend(varNames, loc="best")  # Add legend
plt.grid(axis='both')  # Enable grid lines
plt.show()

# Plot for Memory Latency
plt.figure(figsize=(10, 6))
plt.title("Comparison of 3 Codes (Memory Latency)")
plt.plot(xlocs, code1_mem_latency, "r-o")
plt.plot(xlocs, code2_mem_latency, "b-x")
plt.plot(xlocs, code3_mem_latency, "g-^")
plt.xticks(xlocs, problem_sizes)
plt.xlabel("Problem Sizes")
plt.ylabel("Memory Latency")
plt.legend(varNames, loc="best")  # Add legend
plt.grid(axis='both')  # Enable grid lines
plt.show()

# EOF