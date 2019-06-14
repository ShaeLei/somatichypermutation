## this version is used, to find from the mixcr export assembled seqs, and mixcr export aligned cdrs.
## mixcr generates more cdrs in the export alignments, than in the export clones.
#! usr/bin/python
import os
import sys

if len(sys.argv)!=2:
    sys.exit(0)

wd = sys.argv[1]+'/'
if not os.path.exists(wd):
    os.mkdir(wd)
if not os.path.exists(wd + 'fasta/'):
    os.mkdir(wd + 'fasta/')
if not os.path.exists(wd + 'fasta/singleton'):
    os.mkdir(wd + 'fasta/singleton')
os.system('rm ' + wd + 'fasta/*.fasta')

#shen is sample number, 1-16.
def sep(num):

    map1 = {}
    linenumber = {}
    # k is the line number shown in vim left lane.
    k = 1
    reads = []

    f2 = open('alignments/' + num + '_alignments.txt', 'r')
    f2.readline()
    while True:
        k += 1
        line = f2.readline()
        if not line:
            break
        info = line.split('\t')
        if not ',' in info[0]:
            read = info[0]
        else:
            read = info[0].split(',')[0]
        key = info[20]
        index = read.find(key)
        if key not in map1:
            map1[key] = [read[index:]]
        else:
            map1[key].append(read[index:])
        if key not in linenumber:
            linenumber[key] = str(k)
    f2.close()

# this is to generate separation files one by one.
    for key in map1:
        with open(wd + 'fasta/' + str(linenumber[key]) + '_' + str(len(map1[key])) + '.fasta', 'w') as outf:
            for i in range(len(map1[key])):
                outf.write('>' + str(i+1) + '\n' + map1[key][i] + '\n')

    os.system('mv ' + wd + 'fasta/*_1.fasta ' + wd + 'fasta/singleton')


sep(sys.argv[1])




