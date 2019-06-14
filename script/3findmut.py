#! usr/bin/python
import os
import sys
import glob


def compare_blast_results_to_parental_seq(result_dir, parental_fasta_fn):
    with open(parental_fasta_fn) as f:
        f.readline()
        parentalseq = f.readline().strip()

    if not os.path.exists(result_dir+'cmpr/'):
        os.mkdir(result_dir+'cmpr/')

    for blastfn in glob.glob(result_dir+'blast/*.blast'):
        with open(blastfn) as f:
            blastlines = f.readlines()
        cmprfn = blastfn.replace('blast', 'cmpr')
        with open(cmprfn,'w') as f:
            for line in blastlines:
                seq, qstart, qend = line.split()
                qstart = int(qstart)
                qend = int(qend)
                seq = '-'*(qstart-1)+seq
                diff = ''
                for i in range(qend):
                    if seq[i] == parentalseq[i]:
                        diff += '-'
                    else:
                        diff += seq[i]
                f.write(diff+'\n')


if len(sys.argv)!=2:
    sys.exit(0)


result_dir = sys.argv[1]+'/'
parental_fasta_fn = 'script/parental.fasta'



compare_blast_results_to_parental_seq(result_dir, parental_fasta_fn)
