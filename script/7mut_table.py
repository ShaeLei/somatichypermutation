import numpy as np
import os
import sys

## the input is mut_freq/, output is mut_table/.

num = sys.argv[1]

if not os.path.exists('mut_table/'):
    os.mkdir('mut_table/')

def maketable(fn):
    mp = { 'A' : 0, 'T' : 1, 'C' : 2, 'G' : 3 }

    table = np.zeros((4,4))

    with open(fn) as f:
        lines = f.readlines()

    for line in lines[1:-1]:
        n1, n2, count = line.split()
        count = int(count)
        table[mp[n1]][mp[n2]] = count

    return table.astype(int)


def savetable(tbl, fn):
    tmptbl = tbl.astype(str).tolist()
    header = ['A', 'T', 'C', 'G' ]
    for i in range(4):
        tmptbl[i][i] = '-'
        tmptbl[i].insert(0, header[i])
        tmptbl[i] = '\t'.join(tmptbl[i]) + '\n'

    tmptbl.insert(0, '#\t' + '\t'.join(header) + '\n')

    with open(fn, 'w') as f:
        f.writelines(tmptbl)



name = 'mut_freq/{num}_mut_freq'.format(num = num)
table = maketable(name)
savetable(table, 'mut_table/' + num + '_mut')

#wt = tables[8-1] + tables[14-1]
#het = tables[11-1] + tables[20-1]
#ko = tables[3-1] + tables[6-1] + tables[9-1] + tables[12-1] + tables[16-1] + tables[18-1]

#savetable(wt, 'wt.txt')
#savetable(het, 'het.txt')
#savetable(ko, 'ko.txt')

