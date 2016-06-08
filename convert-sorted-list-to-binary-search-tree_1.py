# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    node = None
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        size = 0
        runner = head
        self.node = head
        while runner:
            runner = runner.next
            size += 1
        return self.inorderHelper(`0, size - 1)
    def inorderHelper(self, start, end):
        if start > end:
            return None
        mid = start + (end - start) / 2
        left = self.inorderHelper(start, mid - 1)
        treenode = TreeNode(self.node.val)
        treenode.left = left
        self.node = self.node.next
        treenode.right = self.inorderHelper(mid + 1, end)
        return treenode
