#! usr/bin/python
import glob
import sys 
import os

if len(sys.argv)!=2:
    sys.exit(0)
num = sys.argv[1]




def template(num):
    with open(num + '/shen' + num + '_mut_v2') as f:
        seqs = f.readlines()


    # seqs is a list, with all mutated templates in a single cdr.

    # seq is a single template.
    # this whole graph is to exclude those without any mutations.
    templates = 0
    for seq in seqs:
        seq = seq.strip()
        count = 0
        for i in range(len(seq)):
            if seq[i] != '-':
                count += 1
        if count > 0:
            templates += 1

    return templates



with open('mutated_templates.txt', 'a') as outf:
    outf.write(str(template(num)) + '\n')
