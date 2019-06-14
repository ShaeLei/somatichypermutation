import os

## 5 is to separate mut_cdr and others.
## 6 and 7 are about mutation spectrum.
### use 7 after 6freq.py is finished.
## 8 is to count total mutation number.
## 9 is to count mutations/template.
## 10 count_templates.py is to count the mutated templates.

def pack(num):

    os.system("python script/1sep.py " + num) # fastq dir+clones dir-> fasta dir
    os.system("python script/2blast.py " + num) # -> blast dir
    os.system("python script/3findmut.py " + num) # -> cmpr
    os.system("python script/4collapse.py " + num) # currently insertion and deletion will be removed
    os.system("python script/5mut.py " + num) # -> mut-cdr dir; exclude 1-count mut
    os.system("python script/catcdr.py " + num)
    os.system("python script/graph2.py " + num)
    os.system("cat {path}/mut_cdr_v2/*_* > {path}/shen{path}_mut_v2".format(path=num))
    os.system("ls " + num + "/collapse/*_* | wc -l >> tcdr")
    os.system("ls " + num + "/fasta/singleton | wc -l >> singletoncdr")
    os.system("ls " + num + "/mut_cdr_v2/*_* | wc -l >> mcdr")

    # 8 and 10 are outf(,'a'). notice this.
    os.system("python script/8count_mut.py " + num)
    os.system("python script/10count_templates.py " + num)
    ##os.system("python script/9count_template.py " + num)

    # 6, 7, 11 are used for mutation spectrum.
    os.system("python script/6freq.py " + num)
    os.system('python script/7mut_table.py ' + num)
    os.system("python script/11calc_spectrum.py " + num)

    #os.system("python script/12hist.py " + num)
    #os.system("python script/13hot_spot_percentage.py " + num)
    #os.system("python hot_mut_spec.py " + num)
    #os.system("python script/hist_percent.py " + num)


os.system("touch tcdr")
os.system("touch mcdr")
os.system("touch singletoncdr")
#for num in range(14):
#    pack(str(num+1))
pack('1')


