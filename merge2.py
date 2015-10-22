class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge(root1, root2):
    node1 = root1
    beforeNode1 = None
    node2 = root2
    while node1 != None and node2 != None:
        if node1.value < node2.value:
            beforeNode1 = node1
            node1 = node1.next
        else:
            temp = node2.next
            if beforeNode1:
                beforeNode1.next = node2
            node2.next = node1
            beforeNode1 = node2
            node2 = temp
    if node2:
        beforeNode1.next = node2
    while root1:
        print root1.value
        root1 = root1.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node3
node3.next = node5

node2.next = node4

        
merge(node2, node1)    

