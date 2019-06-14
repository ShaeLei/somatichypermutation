import sys

num = sys.argv[1]
wd = num + '/'
name = 'shen' + num + '_mut'
length = 180

hot_start = [2, 16, 38, 70, 84, 93, 131, 135, 145, 157, 176]
hot = []
for i in range(len(hot_start)):
    hot.append(hot_start[i]-1)
    hot.append(hot_start[i])
    hot.append(hot_start[i]+1)
    hot.append(hot_start[i]+2)



hist = []
for i in range(length):
    hist.append(0)

with open(wd + name) as f2:
    while True:
        seq = f2.readline().strip('\n')
        if not seq:
            break
        for i in range(length):
            if seq[i] != '-':
                hist[i] += 1

summation = sum(hist)

with open('hist_percent/' + num, 'w') as outf:
    outf.write('Total mutation\t' + str(summation) + '\n')
    for i in range(length):
        percent = float(hist[i]) / summation * 100
        if i in hot:
            outf.write( str(i+1) + '\t' + str(percent) + '\tr\n')
        else:
            outf.write( str(i+1) + '\t' + str(percent) + '\tb\n')
