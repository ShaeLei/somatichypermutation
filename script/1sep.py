## this version is used, assembls are exported by pear. use the cdrs found in the mixcr export clones.
## mixcr generates more cdrs in the export alignments, than in the export clones.
#! usr/bin/python
import os
import sys

if len(sys.argv)!=2:
    sys.exit(0)

num = sys.argv[1]

wd = num + '/'
if not os.path.exists(wd):
    os.mkdir(wd)
if not os.path.exists(wd + 'fasta/'):
    os.mkdir(wd + 'fasta/')
if not os.path.exists(wd + 'fasta/singleton/'):
    os.mkdir(wd + 'fasta/singleton')


#shen is sample number, 1-16.
def sep(num):

    f1 = open('clones/clones' + num + '.txt')
    line = f1.readline()

    with open('fastq/' + num + '.fastq') as f:
        seqs = f.readlines()

    map1 = {}
    linenumber = {}

    k = 1
    for line in f1.readlines():
        key = line.split('\t')[23]
        linenumber[key] = k
        k = k + 1
        for i in range(len(seqs)/4):
            seq = seqs[4*i + 1]

# check vadality.
            flag = True
            for j in range(len(seq)-2):
                if seq[j+1] not in ['A', 'T', 'C', 'G']:
                    flag = False
                    break
            if flag == False:
                continue
################

            index = seq.find(key)
            if index != -1:
                if key not in map1:
                    map1[key] = [seqs[4*i + 1][index:-1]]
                else:
                    map1[key].append(seqs[4*i + 1][index:-1])
    f1.close()

# this is to generate separation files one by one.
    for key in map1:
        with open(wd + 'fasta/' + str(linenumber[key]) + '_' + str(len(map1[key])) + '.fasta', 'w') as outf:
            for i in range(len(map1[key])):
                outf.write('>' + str(i+1) + '\n' + map1[key][i] + '\n')


sep(num)
os.system('mv ' + wd + 'fasta/*_1.fasta ' + wd + 'fasta/singleton/')



