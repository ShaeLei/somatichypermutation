import numpy as np
import sys
import os

name = sys.argv[1]

if not os.path.exists('mut_spec'):
    os.mkdir('mut_spec')
if not os.path.exists('mut_spec/hot'):
    os.mkdir('mut_spec/hot')

with open('mut_table/' + name + '_mut') as f:
#with open('mut_table/' + name + '_mut_hot') as f:
    title = f.readline()
    lines = f.readlines()


atcg = []
line_sums = []
origin = []
for i in range(4):
    lala = lines[i].strip().split('\t')
    origin.append(lala)
    line = np.genfromtxt(lala)
    atcg.append(line)
    line_sum = np.nansum(line)
    line_sums.append(line_sum)

total = sum(line_sums)

weight = [1.07, 0.83, 1.18, 0.98]

tmps2 = []
for i in range(4):
    tmp1 = line_sums[i]/total
    tmp2 = tmp1 * weight[i]
    tmps2.append(tmp2)

total2 = sum(tmps2)


for i in range(4):
    tmp3 = tmps2[i]/total2
    for j in range(len(atcg[i])):
        if not np.isnan(atcg[i][j]):
            origin[i][j] = '%.1f'%(tmp3 * 100 * atcg[i][j] / line_sums[i])
            atcg[i][j] = float(origin[i][j])




tmp5 = []

for j in range(4):
    tmp6 = []
    for i in range(4):
        tmp6.append(atcg[i][j+1])
    tmp5.append('%.1f'%(np.nansum(tmp6)))


tmp7 = '\t'.join(tmp5)


tmp8 = '%.1f'%(float(tmp5[0]) + float(tmp5[1]))
tmp9 = '%.1f'%(float(tmp5[2]) + float(tmp5[3]))

#outf = open('mut_spec/hot/' + name, 'w')
outf = open('mut_spec/' + name, 'w')
outf.write(title)

for i in range(4):
    tmp4 = '\t'.join(origin[i])
    outf.write(tmp4 + '\n')

outf.write('#\t' + tmp7 + '\n')
outf.write('#\t#\t' + tmp8 + '\t#\t' + tmp9 + '\n')
outf.close()

#np.savetxt('mut_spec/' + str(name) + '_mut', origin, fmt='%.1f', delimiter='\t', header=title)
