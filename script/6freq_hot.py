#! /usr/bin/python
# this script is to generate a 3-column table about mutation frequencies.
import sys
import os

## the input is 9/shen9_mut, output is mut_freq

if len(sys.argv)!=2:
    sys.exit(0)

if not os.path.exists('mut_freq/hot/'):
    os.mkdir('mut_freq/hot/')


num = sys.argv[1]
wd = num+'/'

name = wd + 'shenhot' + num + '_mut'

with open(name, 'r') as f:
    lines = f.readlines()

# get the number of entries in 1 file.
entry = len(lines)

if entry > 0:
    countac = 0
    countat = 0
    countag = 0
    countta = 0
    counttc = 0
    counttg = 0
    countca = 0
    countct = 0
    countcg = 0
    countga = 0
    countgt = 0
    countgc = 0
    
    with open('script/parental', 'r') as m:
        mstr = m.readline().strip()
    
    for i in range(entry):
        mutb = lines[i][0:-1]
        for j in range(len(mstr)):
            if len(mutb) < len(mstr):
                mutb += '-'*(len(mstr) - len(mutb))
            if mutb[j] != '-':
                bb = mstr[j] + mutb[j]
                if bb == 'AC':
                    countac=countac + 1
                elif bb == 'AT':
                    countat = countat + 1
                elif bb == 'AG':
                    countag = countag + 1
                elif bb == 'TA':
                    countta = countta + 1
                elif bb == 'TC':
                    counttc = counttc + 1
                elif bb == 'TG':
                    counttg = counttg + 1
                elif bb == 'CA':
                    countca = countca + 1
                elif bb == 'CT':
                    countct = countct + 1
                elif bb == 'CG':
                    countcg = countcg + 1
                elif bb == 'GA':
                    countga = countga + 1
                elif bb == 'GT':
                    countgt = countgt + 1
                elif bb == 'GC':
                    countgc = countgc + 1
    
    with open('mut_freq/hot/' + num + '_mut_freq', 'w') as outf:
        outf.write('Parental\tMutation\tFrequency\n')
        outf.write('A\tC\t' + str(countac) + '\n')
        outf.write('A\tT\t' + str(countat) + '\n')
        outf.write('A\tG\t' + str(countag) + '\n')
        outf.write('T\tC\t' + str(counttc) + '\n')
        outf.write('T\tA\t' + str(countta) + '\n')
        outf.write('T\tG\t' + str(counttg) + '\n')
        outf.write('C\tA\t' + str(countca) + '\n')
        outf.write('C\tT\t' + str(countct) + '\n')
        outf.write('C\tG\t' + str(countcg) + '\n')
        outf.write('G\tA\t' + str(countga) + '\n')
        outf.write('G\tT\t' + str(countgt) + '\n')
        outf.write('G\tC\t' + str(countgc) + '\n')
        outf.write('Total mutation: ' + str(countac + countat + countag + counttc + countta + counttg + countca + countct + countcg + countga + countgt + countgc)+ '\n')
