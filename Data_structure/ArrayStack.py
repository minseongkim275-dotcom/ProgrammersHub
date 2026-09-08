from Dynamic_array import DynamicArray

class ArrayStack():
    def __init__(self):
        self._A = DynamicArray()

    def is_empty(self):
        return len(self._A) == 0

    def __len__(self):
        return len(self._A)

    def push(self,key):
        self._A.append(key)

    def top(self):
        if self.is_empty():
            raise IndexError
        return self._A[len(self._A)-1]

    def pop(self):
        return self._A.pop()



if __name__ == '__main__':
    s = ArrayStack()
    print(s.is_empty())        # True
    s.push(1); s.push(2); s.push(3)
    print(len(s))              # 3
    print(s.top())             # 3
    print(len(s))              # 3  ← top은 제거 안 함
    print(s.pop())             # 3
    print(s.pop())             # 2
    print(s.is_empty())        # False
    print(s.pop())             # 1
    print(s.is_empty())        # True
    s.pop()                    # IndexError
