#! usr/bin/python

str1 = ''
str2 = ''
str3 = ''
mutn = {'A':0, 'T':0, 'C':0, 'G':0, '-':0}
mutb = {}
for base in mutn.keys():
    vals = mutn[base]
    if vals in mutb:
        mutb[vals].append(base)
    else:
        mutb[vals] = [base]
bases = []
for val in sorted(mutb.keys())[::-1]:
    if val == 0:
        pass
    else:
        bases += mutb[val]
    if len(bases) > 2:
        break
bases += ['-']*3
str1 += bases[0]
str2 += bases[1]
str3 += bases[2]

print bases, str1, str2, str3

