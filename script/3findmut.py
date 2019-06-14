#! usr/bin/python
import os
import sys

if len(sys.argv)!=2:
    sys.exit(0)


wd = sys.argv[1]+'/'


if not os.path.exists(wd+'cmpr/'):
    os.mkdir(wd+'cmpr/')

def cmpr(name):
    paren = 'CTACTGGGGTCAAGGAACCTCAGTCACCGTCTCCTCAGGTAAGAATGGCCTCTCCAGGTCTTTATTTTTAACCTTTGTTATGGAGTTTTCTGAGCATTGCAGACTAATCTTGGATATTTGTCCCTGAGGGAGCCGGCTGAGAGAAGTTGGGAAATAAACTGTCTAGGGATCTCAGAGCCT'
    
    with open(wd+'blast/' + name + '_blast', 'r') as f:
        lines = f.readlines()
    outf = open(wd+'cmpr/' + name + '_cmpr', 'w')
    
    
    for i in range(len(lines)):
        line = lines[i].strip().split('\t')
        seq = line[0]
        qstart = int(line[1])
        qend = int(line[2])
        son = ''
        if qstart > 1:
            seq = '-'*(qstart-1) + seq
        for j in range(qend):
            if seq[j] == paren[j]:
                son = son + '-'
            else:
                son = son + seq[j]
        outf.write(son + '\n')
    
    outf.close()


import glob

filelist = []
for fn in glob.glob(wd+'blast/*_blast'):
    filelist.append(fn.split('/')[-1].split('_bla')[0])

for name in filelist:
    cmpr(name)





