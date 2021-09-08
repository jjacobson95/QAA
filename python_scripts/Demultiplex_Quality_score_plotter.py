#!/usr/bin/env python

import Bioinfo
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import argparse

#argparse. 
parser = argparse.ArgumentParser()
parser.add_argument("-R_file", default=1)

args = parser.parse_args()
file = args.R_file


#path locations
# read_file_1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
# index_file_1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
# index_file_2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz"
# read_file_2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"

#this will only work for the two reads with 101 charcters
phred_list =[] 
fred_list =Bioinfo.populate_list(file)
phred_list = fred_list[0]
#sums_list = phred_list[:]
line_count = fred_list[1]

print("phred_list output: ", phred_list)
print("line_count output: ", line_count)

count = 0
for value in phred_list:
    phred_list[count] = value/(line_count/4)
    count += 1



plt.bar(range(101), phred_list)
plt.title('Quality Score Distribution')
plt.xlabel('Base Number')
plt.ylabel('Quality Score Mean')
plt.grid(True)
plt.savefig("/home/jjacobso/bgmp/bioinformatics/Bi623/Assignments/QAA/24_R2.png")
plt.show()





