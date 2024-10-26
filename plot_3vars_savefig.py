"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot, and saves it to a file named "myplot.png"

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

PEAK_MEMORY_BANDWIDTH = 204.8 * 1024 * 1024 * 1024  
MEMORY_ACCESSES = 1e6  
BYTES_ACCESSED = 4 * MEMORY_ACCESSES  
OPS = 1e6  

#plot_fname = "getplot.png"
#fname = "sample_data_3vars.csv"

plot_fname_mflops = "mflopsplot.png"
plot_fname_mem_bw = "bandwidthplot.png"
plot_fname_mem_latency = "latencyplot.png"

fname = "ellerun.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)
print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df['Problem Size'].values.tolist()
elapsed_times_direct = df['sum_direct'].values.tolist()
elapsed_times_indirect = df['sum_indirect'].values.tolist()
elapsed_times_vector = df['sum_vector'].values.tolist()

# MFLOP/s calculations
mflops_direct = [(OPS / time) for time in elapsed_times_direct]
mflops_indirect = [(OPS / time) for time in elapsed_times_indirect]
mflops_vector = [(OPS / time) for time in elapsed_times_vector]

# Bandwidth calculations
memory_bandwidth_direct = [(BYTES_ACCESSED / time) / PEAK_MEMORY_BANDWIDTH * 100 for time in elapsed_times_direct]
memory_bandwidth_indirect = [(BYTES_ACCESSED / time) / PEAK_MEMORY_BANDWIDTH * 100 for time in elapsed_times_indirect]
memory_bandwidth_vector = [(BYTES_ACCESSED / time) / PEAK_MEMORY_BANDWIDTH * 100 for time in elapsed_times_vector]

# Memory Latency calculations
memory_latency_direct = [time / MEMORY_ACCESSES for time in elapsed_times_direct]
memory_latency_indirect = [time / MEMORY_ACCESSES for time in elapsed_times_indirect]
memory_latency_vector = [time / MEMORY_ACCESSES for time in elapsed_times_vector]

plt.figure()
plt.plot(problem_sizes, mflops_direct, label='Direct', marker='o', color='red')
plt.plot(problem_sizes, mflops_indirect, label='Indirect', marker='x', color='blue')
plt.plot(problem_sizes, mflops_vector, label='Vector', marker='^', color='green')
plt.title('Problem Size vs. MFLOP/s')
plt.xlabel('Problem Size')
plt.ylabel('MFLOP/s')
plt.legend()
plt.grid(axis='both')
plt.savefig(plot_fname_mflops, dpi=300)
plt.close() 

plt.figure()
plt.plot(problem_sizes, memory_bandwidth_direct, label='Direct', marker='o', color='red')
plt.plot(problem_sizes, memory_bandwidth_indirect, label='Indirect', marker='x', color='blue')
plt.plot(problem_sizes, memory_bandwidth_vector, label='Vector', marker='^', color='green')
plt.title('Problem Size vs. Memory Bandwidth Utilization')
plt.xlabel('Problem Size')
plt.ylabel('Memory Bandwidth Utilization (%)')
plt.legend()
plt.grid(axis='both')
plt.savefig(plot_fname_mem_bw, dpi=300)
plt.close() 

plt.figure()
plt.plot(problem_sizes, memory_latency_direct, label='Direct', marker='o', color='red')
plt.plot(problem_sizes, memory_latency_indirect, label='Indirect', marker='x', color='blue')
plt.plot(problem_sizes, memory_latency_vector, label='Vector', marker='^', color='green')
plt.title('Problem Size vs. Memory Latency')
plt.xlabel('Problem Size')
plt.ylabel('Memory Latency')
plt.legend()
plt.grid(axis='both')
plt.savefig(plot_fname_mem_latency, dpi=300)
plt.close()

plt.show()  

# EOF