#/usr/bin/python
import os
import glob
import sys

if len(sys.argv)!=2:
    sys.exit(0)

wd = sys.argv[1]+'/'

filelist = []
for fn in glob.glob(wd+'fasta/*.fasta'):
    filelist.append(fn.split('/')[-1].split('.')[0])

if not os.path.exists(wd+'blast/'):
    os.mkdir(wd+'blast/')

# this script is to blast all seqs to the parental.
#filelist = []

#for (dirpath, dirnames, filenames) in os.walk('fasta'):
#    name = filenames[0:filenames.find('.')]
#    filelist.extend(name)

for name in filelist: 
    cmd = "blastn -query script/parental.fasta -subject " + wd + "fasta/" + name + ".fasta -task blastn -max_target_seqs 1000 -out " + wd + "blast/" + name + "_blast -outfmt \"6 sseq qstart qend\""
    os.system( cmd )


