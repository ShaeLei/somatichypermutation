import os

#os.system('rm collect_mut')

for i in range(20):
    num = i + 1
    with open('{num}/shen{num}_mut'.format(num = num), 'r') as f:
        lines = f.readlines()
    with open('collect_mut', 'a') as outf:
        outf.write('********************{num}*********************\n'.format(num = num))
        for line in lines:
            outf.write(line)

