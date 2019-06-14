#/usr/bin/python
import os
import glob
import sys

def blast_against_parental_seq(result_dir, parental_fasta_fn):
    if not os.path.exists(result_dir+'blast/'):
        os.mkdir(result_dir+'blast/')

    for fastafn in glob.glob(result_dir+'fasta/*.fasta'):
        blastfn = fastafn.replace('fasta', 'blast')
        os.system('blastn -query '+parental_fasta_fn+' -subject '+fastafn+' -task blastn -max_target_seqs 1000 -out '+blastfn+' -outfmt \"6 sseq qstart qend\"')


if len(sys.argv)!=3 and len(sys.argv)!=2:
    print sys.argv[0]+' <result_folder> <parental_fasta_file>'
    sys.exit(0)

result_dir = sys.argv[1]+'/'
parental_fasta_fn = 'script/parental.fasta'

blast_against_parental_seq(result_dir, parental_fasta_fn)
