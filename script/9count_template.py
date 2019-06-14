#! usr/bin/python
import glob
import sys
import os

if len(sys.argv)!=2:
    sys.exit(0)
wd = sys.argv[1]+'/'

dic = {}
with open(wd+'shen' + sys.argv[1] + '_mut_v2') as f:
    seqs = f.readlines()

#total is a str that concatenates all lines in one cdr.
#cannot see any usage of total.
total = ''
for seq in seqs:
    total += seq.strip()

#count is the mutation number in one cdr.
linenum = 0
for seq in seqs:
    seq = seq[0:-1]
    count = 0
    for i in range(180):
        if seq[i] != '-':
            count += 1
    if count > 0:
        linenum += 1
        if count in dic:
            dic[count] += 1
        else:
            dic[count] = 1



with open('template_mutations_v2.txt', 'a') as outf:
    outf.write('----------' + sys.argv[1] + '-----------\n')
    outf.write('mutational templates # \t' + str(linenum) + '\n')
    for count in sorted(dic.keys()):
        outf.write(str(count) + '\t' + str(dic[count]) + '\n')
