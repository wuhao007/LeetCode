class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = None
class Solution:
    def reverse(self, head):
        
        dummy = head.next
        head.next = None
        cur = dummy
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        dummy.next = prev
        return dummy
    def print_tree(self, tree):
        while tree:
            print tree.val, '->'
            tree = tree.next
nodeA = ListNode('A')
nodeB = ListNode('B')
nodeC = ListNode('C')
nodeD = ListNode('D')
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeA
solution = Solution()
#solution.print_tree(nodeA)
node = solution.reverse(nodeA)
solution.print_tree(node)

