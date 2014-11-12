'''
Programming assignment 4:

implement the Kosaraju's
algorithm for computing
strongly connected components (SCC's)
in the given directed graph.

Find 5 largest SCC's.

'''

import sys

def readDirectedGraph(filename):
    f = open(filename)
    adjlist = []
    line = f.readline()
    while line != '':
        num1, num2 = line.split()
        v_from = int(num1)
        v_to = int(num2)
        while len(adjlist) < max(v_from, v_to):
            adjlist.append([])
        adjlist[v_from - 1].append(v_to - 1)
        line = f.readline()
    return adjlist

def dfs(G, v, onStack, marked, cycle):
    onStack[v] = True
    marked[v] = True
    for w in G[v]:
        if len(cycle) > 0:
            return
        elif not marked[w]:
            dfs(G, w, onStack, marked, cycle)
        elif onStack[w]:
            cycle += [w]
            return
    onStack[v] = False

def directedCycle(G):
    n = len(G)
    marked = [False] * n
    onStack = [False] * n
    cycle = []
    for v in range(n):
        if not marked[v]:
            dfs(G, v, onStack, marked, cycle)
    return cycle

def main():
    graph = readDirectedGraph('SCC.txt')
    print directedCycle(graph)

main()   
