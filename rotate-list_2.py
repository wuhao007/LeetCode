        if head==None:
            return head
        curNode = head
        size = 1
        while curNode!=None:
            size += 1
            curNode = curNode.next
        size -= 1
        k = k%size
        if k==0:
            return head
        len = 1
        curNode = head
        while len<size-k:
            len += 1
            curNode = curNode.next
        newHead = curNode.next
        curNode.next = None
        curNode = newHead
        while curNode.next!=None:
            curNode = curNode.next
        curNode.next = head
        return newHead
