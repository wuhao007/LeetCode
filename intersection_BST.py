class TreeNode:
    def __init__(self, value):
        self.val = value
        self.parent = None
        self.left = None
        self.right = None

class Solution:
    def inorder(self, lastNode, root):
        while root:
            if lastNode == root.parent:
                if root.left:
                    lastNode = root
                    root = root.left
                    continue
                else:
                    lastNode = None
            if lastNode == root.left:
                return lastNode, root
                if root.right:
                    lastNode = root;
                    root = root.right;
                    continue;
                else:
                    lastNode = None
            if lastNode == root.right:
                lastNode = root
                root = root.parent

    def inorder2(self, lastNode, root):
        while root:
            if lastNode == root.left:
                if root.right:
                    lastNode = root;
                    root = root.right;
                    continue;
                else:
                    lastNode = None
            if lastNode == root.right:
                lastNode = root
                root = root.parent
            if root is None:
                return lastNode, root
            if lastNode == root.parent:
                if root.left:
                    lastNode = root
                    root = root.left
                    continue
                else:
                    lastNode = None
            if lastNode == root.left:
                return lastNode, root

    def getSuccessor(self, cur):
        if cur.right:
            cur = cur.right
            while cur.left:
                cur = cur.left
        elif cur.parent:
            while cur.parent is not None and cur == cur.parent.right: 
                cur = cur.parent
            cur = cur.parent if cur.parent else None
        else: 
            cur = None
        return cur;
    
    def intersection(self, head1, head2):
        node1 = head1
        while node1.left:
            node1 = node1.left
        node2 = head2
        while node2.left:
            node2 = node2.left
        ret = []
        while node1 is not None and node2 is not None:
            print node1.val, node2.val
            if node1.val < node2.val:
                node1 = self.getSuccessor(node1)
            elif node1.val == node2.val: 
                ret += [node1.val]
                node1 = self.getSuccessor(node1)
            else:
                node2 = self.getSuccessor(node2)
        return ret
                
first1 = TreeNode(1)
first2 = TreeNode(2)
first3 = TreeNode(3)
first4 = TreeNode(4)
first5 = TreeNode(5)
first6 = TreeNode(6)
first7 = TreeNode(7)
first4.left = first2
first4.right = first6

first2.left = first1
first2.right = first3
first2.parent = first4

first6.left = first5
first6.right = first7
first6.parent = first4

first1.parent = first2
first3.parent = first2
first5.parent = first6
first7.parent = first6

second1 = TreeNode(1)
second2 = TreeNode(2)
second3 = TreeNode(3)
second4 = TreeNode(4)
second5 = TreeNode(5)
second6 = TreeNode(6)
second7 = TreeNode(7)
second4.left = second2
second4.right = second6

second2.left = second1
second2.right = second3
second2.parent = second4

second6.left = second5
second6.right = second7
second6.parent = second4

second1.parent = second2
second3.parent = second2
second5.parent = second6
second7.parent = second6

solution = Solution()
print solution.intersection(first4, second4)
