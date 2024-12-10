from collections import deque

class Queue:
    def __init__(self):
        self._d = deque()

    def enqueue(self, val):
        self._d.append(val)

    def dequeue(self):
        if not self._d:
            raise IndexError("dequeue from empty queue")
        return self._d.popleft()

    def is_empty(self):
        return len(self._d) == 0

    def __len__(self):
        return len(self._d)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1); q.enqueue(2)
    print(q.dequeue(), len(q))