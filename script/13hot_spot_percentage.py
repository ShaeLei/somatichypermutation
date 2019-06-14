#! /usr/bin/python
# this file is to count the in-hot-spot mutation numbers in each sample.
# this should be the version 1 counting.
import sys

if len(sys.argv)!=2:
    sys.exit(0)

num = sys.argv[1]
wd = num+'/'

name = wd + 'shen' + num + '_mut'

hot_start = [2, 16, 38, 70, 84, 93, 131, 135, 145, 157, 176]
hot = []
for i in range(len(hot_start)):
    hot.append(hot_start[i]-1)
    hot.append(hot_start[i])
    hot.append(hot_start[i]+1)
    hot.append(hot_start[i]+2)


with open(name, 'r') as f:
    lines = f.readlines()


count = 0
for seq in lines:
    seq = seq.strip()
    for i in range(len(seq)):
        if i in hot and seq[i] != '-':
            count += 1

###########with open('hot_spot_total_mutation', 'a') as f:
with open('hot_spot_total_mutation.txt', 'a') as f:
    f.write(num + '\t' + str(count) + '\n')
