#! usr/bin/python
import glob
import sys 
import os

if len(sys.argv)!=2:
    sys.exit(0)
num = sys.argv[1]
wd = num +'/'



filelist = []
for fn in glob.glob(wd + 'mut_cdr/*'):
    filelist.append(fn.split('/')[-1])

with open(wd + 'shen' + num + '_mut', 'w') as outf:
    for fn in filelist:
        outf.write(fn + '\n')
        with open(wd + 'mut_cdr/' + fn) as f:
            while True:
                line = f.readline()
                outf.write(line)
                if not line:
                    break
