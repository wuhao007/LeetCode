def mergeTwoLists(self, l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    dummy = ListNode(0)
    tmp = dummy
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    if l1:
        tmp.next = l1
    else:
        tmp.next = l2
    return dummy.next
    
def mergeKLists(self, lists):
    if not lists: 
        return None
    end = len(lists) - 1
    while end > 0:
        begin = 0
        while begin < end:
            lists[begin] = self.mergeTwoLists(lists[begin], lists[end]);
            begin += 1
            end -= 1
    return lists[0]
