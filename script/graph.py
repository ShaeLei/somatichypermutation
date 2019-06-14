#! usr/bin/python


def SeqDiff(seq1, seq2):
    diff = ''
    for i in range(len(seq1)):
        if seq1[i]==seq2[i]:
            diff += '-'
        else:
            diff += seq2[i]
    return diff


class Node:
    def __init__(self, seq, id):
        self.id = id
        self.A = set()
        self.T = set()
        self.C = set()
        self.G = set()
        for i in range(len(seq)):
            if seq[i] == 'A':
                self.A.add(i)
            elif seq[i] == 'T':
                self.T.add(i)
            elif seq[i] == 'C':
                self.C.add(i)
            elif seq[i] == 'G':
                self.G.add(i)
    def __str__(self):
        return 'ID: '+str(self.id)+'  |  A: '+str(self.A)+'  |  T: '+str(self.T)+'  |  C: '+str(self.C)+'  |  G: '+str(self.G)


def NodeDis(node1, node2):
    dis = 0
    if node1.A.issubset(node2.A):
        dis += len(node2.A) - len(node1.A)
    else:
        return -1
    if node1.T.issubset(node2.T):
        dis += len(node2.T) - len(node1.T)
    else:
        return -1
    if node1.C.issubset(node2.C):
        dis += len(node2.C) - len(node1.C)
    else:
        return -1
    if node1.G.issubset(node2.G):
        dis += len(node2.G) - len(node1.G)
    else:
        return -1

    return dis



#def ProcessPathes(paths):
#    tmppaths = sorted(paths, key=len)[::-1]
#    print tmppaths
#    usedends = set()
#    newpaths = []
#    for i in range(len(tmppaths)):
#        if tmppaths[i][-1] not in usedends:
#            newpaths.append(tmppaths[i])
#            usedends.add(tmppaths[i][-1])
#        else:
#            while tmppaths[i][-1] in usedends:
#                tmppaths[i].pop()
#            if len(tmppaths[i]) > 1:
#                newpaths.append(tmppaths[i])
#                usedends.add(tmppaths[i][-1])
#    return newpaths


import networkx as nx



def FindPaths2(g):
    graph = nx.DiGraph(g)
    paths = []
    while graph.size()>0:
        mstart = None
        mend = None
        for start in [x for x in graph.nodes() if graph.in_degree(x) == 0]:
            for end in [x for x in graph.nodes() if graph.out_degree(x) == 0]:
                tobreak = False

                tmp = list(nx.all_simple_paths(graph, start, end))
                if len(tmp)==0:
                    continue
                maxpath = sorted(tmp, key=len)[-1]
                paths.append(maxpath)
                graph.remove_node(maxpath[-1])
                tobreak = True
                break
            if tobreak:
                break
    paths = sorted(paths, key=len)
    pathsets = [set(path) for path in paths]
    keeps = [True] * len(pathsets)
    for i in range(len(pathsets)-1):
        for j in range(i+1, len(pathsets)):
            if pathsets[i]<=pathsets[j]:
                keeps[i]=False
    finalpaths = []
    for i in range(len(keeps)):
        if keeps[i]:
            finalpaths.append(paths[i])

    return finalpaths





def FindPaths(g):
    graph = nx.DiGraph(g)
    paths = []
    while graph.size()>0:
        for start in [x for x in graph.nodes() if graph.in_degree(x) == 0]:
            for end in [x for x in graph.nodes() if graph.out_degree(x) == 0]:
                tobreak = False

                tmp = list(nx.all_simple_paths(graph, start, end))
                if len(tmp)==0:
                    continue
                maxpath = sorted(tmp, key=len)[-1]
                paths.append(maxpath)
                graph.remove_node(maxpath[-1])
                tobreak = True
                break
            if tobreak:
                break
    paths = sorted(paths, key=len)
    pathsets = [set(path) for path in paths]
    keeps = [True] * len(pathsets)
    for i in range(len(pathsets)-1):
        for j in range(i+1, len(pathsets)):
            if pathsets[i]<=pathsets[j]:
                keeps[i]=False
    finalpaths = []
    for i in range(len(keeps)):
        if keeps[i]:
            finalpaths.append(paths[i])

    return finalpaths


def ProcessFile(fn):
    with open(fn) as f:
        seqs = f.readlines()
    for i in range(len(seqs)):
        seqs[i] = seqs[i].strip()

    nodes = {}
    nodeids = []
    for i in range(len(seqs)):
        seq = seqs[i]
        if 'A' in seq or 'T' in seq or 'C' in seq or 'G' in seq:
            nodes[i] = Node(seq, i)
            nodeids.append(i)

    dislist = []
    for i in nodeids:
        for j in nodeids:
            dis = NodeDis(nodes[i], nodes[j])
            if dis>0:
                dislist.append((i,j,dis))

    graph = nx.DiGraph()
    graph.add_nodes_from(nodeids)
    graph.add_weighted_edges_from(dislist)

    paths = FindPaths(graph)
    print paths

    newseqs = list(seqs)
    for path in paths:
        for i in range(1, len(path)):
            newseqs[path[i]] = SeqDiff(seqs[path[i-1]], seqs[path[i]])

    return newseqs




#ProcessFile('9/mut_cdr/10_875')

#import sys
#sys.exit(0)






import glob
import sys
import os

if len(sys.argv)!=2:
    sys.exit(0)
wd = sys.argv[1]+'/'


if not os.path.exists(wd + 'mut_cdr_v2/'):
    os.mkdir(wd + 'mut_cdr_v2/')


for fn in glob.glob(wd + 'mut_cdr/*_*'):
    print fn
    outseqs = ProcessFile(fn)
    outfn = fn.replace('mut_cdr','mut_cdr_v2')
    with open(outfn,'w') as f:
        for seq in outseqs:
            f.write(seq+'\n')
