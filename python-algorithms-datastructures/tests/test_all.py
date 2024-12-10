from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.linked_list import LinkedList

def test_sorts():
    arr = [5,3,1,4,2]
    assert bubble_sort(arr) == [1,2,3,4,5]
    assert merge_sort(arr) == [1,2,3,4,5]
    assert quick_sort(arr) == [1,2,3,4,5]

def test_ds():
    s = Stack(); s.push(1); s.push(2)
    assert s.pop() == 2
    q = Queue(); q.enqueue(1); q.enqueue(2)
    assert q.dequeue() == 1
    ll = LinkedList(); ll.append(10); ll.append(20)
    assert ll.to_list() == [10,20]

if __name__ == "__main__":
    test_sorts(); test_ds()
    print("All tests passed")