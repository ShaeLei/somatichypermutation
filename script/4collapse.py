#! usr/bin/python
import glob
import sys 
import os
from collections import Counter
import re


def screen_seq_cmpr(result_dir):
    if not os.path.exists(result_dir + 'collapse/'):
        os.mkdir(result_dir + 'collapse/')

    for cmprfn in glob.glob(result_dir+'cmpr/*.cmpr'):
        with open(cmprfn) as f:
            seqs = f.readlines()

        for i in range(len(seqs)):
            seqs[i] = seqs[i].strip()

        # we make the seqs to the same length
        # find the longest seq, add '-' to the shorter ones.
        maxlen = 0
        for seq in seqs:
            if maxlen<len(seq):
                maxlen = len(seq)
        for i in range(len(seqs)):
            seqs[i] += '-'*(maxlen-len(seqs[i]))

        seqcounter = Counter(seqs)

        def has_break(seq):
            mutsegs = re.split('-+',seq)
            for seg in mutsegs:
                if len(seg)>4:
                    return True
            return False

        collapsefn = cmprfn.replace('cmpr', 'collapse')
        with open(collapsefn, 'w') as f:
            for seq in seqcounter:
                if seqcounter[seq] == 1:
                    pass #TODO
                elif has_break(seq):
                    pass #TODO
                else:
                    f.write(seq + '\n'  )




if len(sys.argv)!=2:
    sys.exit(0)

result_dir = sys.argv[1]+'/'

screen_seq_cmpr(result_dir)
