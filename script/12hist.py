import sys

num = sys.argv[1]
wd = num + '/'
name = 'shen' + num + '_mut'
length = 180
with open('script/parental') as f1:
    parental = f1.readline()

with open(wd + name) as f2:
    seqs = f2.readlines()

with open('script/coord') as f3:
    coord = f3.readline()

info = []
for i in range(length):
    info.append([])

for seq in seqs:
    seq = seq[0:-1]
    for i in range(length):
        if seq[i] != '-':
            info[i].append(seq[i])

lens = []
for i in range(length):
    lens.append(len(info[i]))

max_len = max(lens)


for i in range(length):
    for j in range(max_len-len(info[i])):
        info[i] += [' ']

with open('hist/' + num + '_hist', 'w') as outf:
    outf.write('*************************Sample' + num + '*************************\n')
    outf.write(coord)
    outf.write(parental)
    for i in range(max_len):
        mut = ''
        for j in range(length):
            mut += info[j][i]
        outf.write(mut + '\n')
