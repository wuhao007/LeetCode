def recoverTree( self, root ):
    parent, tmp, pre, first, second = root, None, None, None, None
    while None != parent:
      if None == parent.left:
        if None != pre and pre.val > parent.val:
            second = parent
            if first == None: first = pre
        pre = parent
        parent = parent.right
      else:
        tmp = parent.left
        while None != tmp.right and parent != tmp.right:
          tmp = tmp.right
 
        if None == tmp.right:
          tmp.right = parent
          parent = parent.left
        else:
            if None != pre and pre.val > parent.val:
                second = parent
                if first == None: first = pre
            tmp.right = None
            pre = parent
            parent = parent.right
    first.val, second.val = second.val, first.val
    return root
