import ctypes

class ArrayQueue():
    def __init__(self):
        self._n = 0
        self._front = 0
        self._capacity = 10
        self._A = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def first(self):
        if self.is_empty():
            raise IndexError("빈 큐입니당")
        return self._A[self._front]
      
    def enqueue(self,e):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[(self._front+self._n)%self._capacity] = e
        self._n += 1
        

    def dequeue(self):
        if self._A[self._front] is None:
            raise IndexError("큐가 비어있습니다.")
        tmp = self._A[self._front]
        self._A[self._front] = None
        self._front += 1
        self._front = (self._front) % self._capacity
        self._n -= 1
        return tmp

    def _resize(self,capacity):
        B = self._make_array(capacity)
        for i in range(self._n):
            B[i] = self._A[(self._front+i) % self._capacity]
        self._A = B
        self._front = 0
        self._capacity = capacity
       


if __name__ == '__main__':
    q = ArrayQueue()
    for i in range(5):
        q.enqueue(i)
    print(q.dequeue(), q.dequeue())   # 0 1
    print(q.first(), len(q))          # 2 3

    # 순환 확인: 앞을 비우고 다시 채워서 wrap-around 유도
    for i in range(10, 20):
        q.enqueue(i)
    while not q.is_empty():
        print(q.dequeue(), end=' ')

    print()
    q = ArrayQueue()
    for i in range(15):
        q.enqueue(i)
    print(q._capacity, len(q._A))   # 두 숫자가 같아야 함
# 2 3 4 10 11 12 ... 19 순서로 나와야 함