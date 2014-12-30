class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def interleave(p, q):
    dummy = ListNode(0)
    cur = dummy
    while p is not None and q is not None:
        cur.next = p
        cur = cur.next
        p = p.next
        cur.next = q
        cur = cur.next
        q = q.next
    if p is not None:
        cur.next = p
    elif q is not None:
        cur.next = q
    return dummy.next
def print_list(head):
    path = ''
    while head:
        path += (str(head.val) + '->')
        head = head.next
    return path
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node5.next = node6
print print_list(interleave(node1, node5))
