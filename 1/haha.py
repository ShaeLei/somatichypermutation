import glob
import os
for fn in glob.glob('*_collapse'):
    nfn = fn.replace('_collapse','.collapse')
    os.system('mv '+fn+' '+nfn)
