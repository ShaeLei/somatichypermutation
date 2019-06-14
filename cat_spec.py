import os.path


outf = open('cat_spec_v2.txt', 'w')
dic1 = {1:'A11', 2:'B11', 3:'C11', 4:'D11', 5:'E11', 6:'F11', 7:'G11', 8:'H11', 9:'A12', 10:'B12', 11:'C12', 12:'D12', 13:'E12', 14:'F12'}
for i in range(14):
    name = str(i+1)
    if os.path.isfile('mut_spec/' + name):
        with open('mut_spec/' + name) as f:
            lines = f.readlines()
        outf.write('Sample' + name + '\t' + dic1[i+1] + '\n')
        for line in lines:
            outf.write(line)
        outf.write('\n')


outf.close()
