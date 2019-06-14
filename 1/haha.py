import glob
import os
for fn in glob.glob('*_cmpr'):
    nfn = fn.replace('_cmpr','.cmpr')
    os.system('mv '+fn+' '+nfn)
