class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):
        out=[]
        cur=self.head
        while cur:
            out.append(cur.val); cur=cur.next
        return out

if __name__ == "__main__":
    ll = LinkedList(); ll.append(1); ll.append(2)
    print(ll.to_list())