Q: Given two nodes in a binary tree, find the lowest common ancestor of both nodes. 
The function you should create should take the two nodes as parameters. 
The nodes have left child, right child, and parent pointers. 

example

            A
          /   \
         B     C
        / \   / \
       D   E F   G
        \   
         H

Given F,G output C
Given H,E output B

Input - A,H

node1=A
path1 = {A}
node2 =H

node1=A
path1 = {A}
node2 =D

node1=A
path1 = {A}
node2 =B

node1=A
path1={A}
node2 =A

return A

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None

def to_parent(node1, node2):
    if node1 is None or node2 is None:
        return None
    path1 = set([])
    while node1 is not None or node2 is not None:
        path1.add(node1)
        if node1.parent is not None:
            node1 = node1.parent
        if node2 in path1:
            return node2
        if node2.parent is not None:
            node2 = node2.parent
        if node1.parent is None and node2.parent is None:
            return None
    else:
        return None

A,A
node1 = A
path1 ={A}
node2 = A

n
n^2
