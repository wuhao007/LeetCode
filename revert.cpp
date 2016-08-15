#include<iostream>
Node * revert(Node* head) {
    Node* pre = NULL;
    Node* cur;
    cur = head;
    while (cur != NULL) {
        Node* next = cur.next;
        cur.next = pre;
        pre = cur;
        cur = next;
    }
    return pre;
}
