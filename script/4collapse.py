#! usr/bin/python
import glob
import sys 
import os

if len(sys.argv)!=2:
    sys.exit(0)
wd = sys.argv[1]+'/'

if not os.path.exists(wd + 'collapse/'):
    os.mkdir(wd + 'collapse/')

filelist = []
for fn in glob.glob(wd + 'cmpr/*_cmpr'):
    filelist.append(fn.split('/')[-1].split('_cmpr')[0])


def common(name):
    with open(wd + 'cmpr/' + name + '_cmpr') as f:
        seqs = f.readlines()
    for i in range(len(seqs)):
        seqs[i] = seqs[i].strip()

    # we make the seqs to the same length
    # find the longest seq, add '-' to the shorter ones.
    lens = []
    for seq in seqs:
        lens.append(len(seq))
    if not len(lens) == 0:
        max_len = max(lens)

        for i in range(len(seqs)):
            if len(seqs[i]) < max_len:
                seqs[i] += '-'*(max_len-len(seqs[i]))

        dic = {}
        for i in range(len(seqs)):
            if seqs[i] in dic:
                dic[seqs[i]] += 1
            else:
                dic[seqs[i]] = 1

        outf = open(wd + 'collapse/' + name + '_collapse', 'w')
        for seq in dic:
            breakHappned = False
            for i in range(len(seq)-9):
                tmp = 0
                for j in range(10):
                    if seq[i+j] != '-':
                        tmp += 1
                if tmp > 4:
                    breakHappned=True
                    break

            if dic[seq] > 1 and not breakHappned:
                outf.write(seq + '\n'  )
        outf.close()

        ###str1 = ''
        ###str2 = ''
        ###str3 = ''
        ###for i in range(max_len):
        ###    ithcol = []
        ###    mutn = {'A':0, 'T':0, 'C':0, 'G':0, '-':0}
        ###    mutb = {}
        ###    for seq in seqs:
        ###        mutn[seq[i]] += 1
        ###    for base in mutn.keys():
        ###        vals = mutn[base]
        ###        if vals in mutb:
        ###            mutb[vals].append(base)
        ###        else:
        ###            mutb[vals] = [base]
        ###    bases = []
        ###    for val in sorted(mutb.keys())[::-1]:
        ###        if val < 2:
        ###            pass
        ###        else:
        ###            bases += mutb[val]
        ###        if len(bases) > 3:
        ###            os.system( 'print {wd}{name} >> strange'.format(wd = wd, name = name))
        ###    bases += ['-']*3
        ###    str1 += bases[0]
        ###    str2 += bases[1]
        ###    str3 += bases[2]

        ###outf = open(wd + 'collapse/' + name + '_collapse', 'w')
        ###outf.write(str1 + '\n' + str2 + '\n' + str3 + '\n' )
        ###outf.close()

for name in filelist:
    common(name)
