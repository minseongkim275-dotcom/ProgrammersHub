import ctypes
class DynamicArray():
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self,capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        if not ( 0 <= key < self._n):
            raise IndexError
        return self._A[key]

    def append(self,num):
        if self._n == self._capacity:
            self._resize(self._capacity*2)
        self._A[self._n] = num
        self._n += 1

    def _resize(self, new_capacity):
        B = self._make_array(new_capacity)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = new_capacity

    def pop(self):
        if self._n <= 0:
            raise IndexError
        self._n -= 1
        tmp = self._A[self._n]
        self._A[self._n] = None
        return tmp


if __name__ == '__main__':            
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
        print(len(arr), arr._capacity)
    print(arr[3], arr[9])
    arr.pop()
    arr.pop()
    arr.pop()
    for i in range(7):
        print(arr[i])