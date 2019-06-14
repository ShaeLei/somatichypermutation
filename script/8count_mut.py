#! /usr/bin/python
# this file is to count the total mutation numbers in each sample.
# this should be the version 1 counting.
import sys

if len(sys.argv)!=2:
    sys.exit(0)

num = sys.argv[1]
wd = num+'/'

name = wd + 'shen' + num + '_mut_v2'

with open(name, 'r') as f:
    lines = f.readlines()

total = ''
for seq in lines:
    total += seq.strip()

count = 0
for i in range(len(total)):
    if total[i] != '-':
        count += 1

with open('total_mutation_v2.txt', 'a') as f:
    f.write(num + '\t' + str(count) + '\n')
