#! usr/bin/python
import glob
import sys
import os

if len(sys.argv)!=2:
    sys.exit(0)
wd = sys.argv[1]+'/'

if not os.path.exists(wd + 'mut_cdr/'):
    os.mkdir(wd + 'mut_cdr/')

filelist = []
for fn in glob.glob(wd + 'collapse/*_collapse'):
    filelist.append(fn.split('/')[-1].split('_coll')[0])

def mutcdr(name):
    with open(wd + 'collapse/' + name + '_collapse', 'r') as f:
        seqs = f.readlines()

    if not len(seqs) == 0:
        total = ''
        for seq in seqs:
            total += seq.strip()

        count = 0
        for i in range(len(total)):
            if total[i] != '-':
                count += 1

        if count > 0:
            os.system("cp {wd}collapse/{name}_collapse {wd}mut_cdr/{name}".format(wd=wd, name=name))

for name in filelist:
    mutcdr(name)
