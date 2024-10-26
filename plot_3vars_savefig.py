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

OPERATIONS_PER_MFLIP = 1e6  
DATA_ACCESS_BYTES = 1e9  
MAX_MEMORY_BANDWIDTH = 100  
MEMORY_ACCESS_COUNT = 1e6 

#plot_fname = "getplot.png"

#fname = "sample_data_3vars.csv"

fname = "ellerun.csv"
df = pd.read_csv(fname, comment="#")
print(df)

#var_names = list(df.columns)
#print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df['Problem Size'].values.tolist()
direct_times = df['sum_direct'].values.tolist()
vector_times = df['sum_vector'].values.tolist()
indirect_times = df['sum_indirect'].values.tolist()

# Calculate MFLOP/s
direct_mflops = [OPERATIONS_PER_MFLIP / t for t in direct_times]
vector_mflops = [OPERATIONS_PER_MFLIP / t for t in vector_times]
indirect_mflops = [OPERATIONS_PER_MFLIP / t for t in indirect_times]

# Calculate Memory Bandwidth Utilization (%)
direct_memory_bw = [(DATA_ACCESS_BYTES / t) / MAX_MEMORY_BANDWIDTH * 100 for t in direct_times]
vector_memory_bw = [(DATA_ACCESS_BYTES / t) / MAX_MEMORY_BANDWIDTH * 100 for t in vector_times]
indirect_memory_bw = [(DATA_ACCESS_BYTES / t) / MAX_MEMORY_BANDWIDTH * 100 for t in indirect_times]

# Calculate Memory Latency
direct_memory_latency = [t / MEMORY_ACCESS_COUNT for t in direct_times]
vector_memory_latency = [t / (2 * MEMORY_ACCESS_COUNT) for t in vector_times]
indirect_memory_latency = [t / (3 * MEMORY_ACCESS_COUNT) for t in indirect_times]

# Plot MFLOP/s
plt.figure()
plt.plot(problem_sizes, direct_mflops, label='Direct Sum', marker='o', color='r')
plt.plot(problem_sizes, vector_mflops, label='Vector Sum', marker='x', color='b')
plt.plot(problem_sizes, indirect_mflops, label='Indirect Sum', marker='^', color='g')
plt.title('Problem Size vs. MFLOP/s')
plt.xlabel('Problem Size')
plt.ylabel('MFLOP/s')
plt.legend()
plt.grid(True)
plt.savefig('mflops_plot.png')

# Plot Memory Bandwidth Utilization
plt.figure()
plt.plot(problem_sizes, direct_memory_bw, label='Direct Sum', marker='o', color='r')
plt.plot(problem_sizes, vector_memory_bw, label='Vector Sum', marker='x', color='b')
plt.plot(problem_sizes, indirect_memory_bw, label='Indirect Sum', marker='^', color='g')
plt.title('Problem Size vs. Memory Bandwidth Utilization (%)')
plt.xlabel('Problem Size')
plt.ylabel('Memory Bandwidth Utilization (%)')
plt.legend()
plt.grid(True)
plt.savefig('memory_bandwidth_plot.png')

# Plot Memory Latency
plt.figure()
plt.plot(problem_sizes, direct_memory_latency, label='Direct Sum', marker='o', color='r')
plt.plot(problem_sizes, vector_memory_latency, label='Vector Sum', marker='x', color='b')
plt.plot(problem_sizes, indirect_memory_latency, label='Indirect Sum', marker='^', color='g')
plt.title('Problem Size vs. Memory Latency')
plt.xlabel('Problem Size')
plt.ylabel('Memory Latency (s)')
plt.legend()
plt.grid(True)
plt.savefig('memory_latency_plot.png')

# Show all plots
plt.show()

# EOF