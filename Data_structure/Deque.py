"""
Deque (덱) - 원형 배열 기반
양쪽 끝에서 O(1) 삽입/삭제.

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""
import ctypes


class ArrayDeque:
    DEFAULT_CAPACITY = 8

    def __init__(self):
        self._capacity = self.DEFAULT_CAPACITY
        self._A = self._make_array(self._capacity)
        self._front = 0
        self._n = 0

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        # 원소 개수
        pass

    def is_empty(self):
        pass

    def first(self):
        # 맨 앞 원소 (제거 X) / 비었으면 IndexError
        pass

    def last(self):
        # 맨 뒤 원소 (제거 X) / 비었으면 IndexError
        pass

    def add_first(self, e):
        # 앞에 삽입. 꽉 찼으면 _resize(2 * capacity)
        # 힌트: front 를 한 칸 뒤로 (front - 1) % capacity
        pass

    def add_last(self, e):
        # 뒤에 삽입. 꽉 찼으면 _resize(2 * capacity)
        # 힌트: 뒤 인덱스 = (front + n) % capacity
        pass

    def delete_first(self):
        # 앞에서 제거 후 값 반환 / 비었으면 IndexError
        pass

    def delete_last(self):
        # 뒤에서 제거 후 값 반환 / 비었으면 IndexError
        pass

    def _resize(self, capacity):
        # 새 배열로 옮기면서 front 를 0으로 정렬
        pass

    def __str__(self):
        parts = []
        for i in range(self._n):
            parts.append(str(self._A[(self._front + i) % self._capacity]))
        return '[' + ', '.join(parts) + ']'


# ==================== 정답 ====================
# class ArrayDeque:
#     DEFAULT_CAPACITY = 8
#
#     def __init__(self):
#         self._capacity = self.DEFAULT_CAPACITY
#         self._A = self._make_array(self._capacity)
#         self._front = 0
#         self._n = 0
#
#     def _make_array(self, capacity):
#         return (capacity * ctypes.py_object)()
#
#     def __len__(self):
#         return self._n
#
#     def is_empty(self):
#         return self._n == 0
#
#     def first(self):
#         if self.is_empty():
#             raise IndexError('덱이 비어있습니다')
#         return self._A[self._front]
#
#     def last(self):
#         if self.is_empty():
#             raise IndexError('덱이 비어있습니다')
#         return self._A[(self._front + self._n - 1) % self._capacity]
#
#     def add_first(self, e):
#         if self._n == self._capacity:
#             self._resize(2 * self._capacity)
#         self._front = (self._front - 1) % self._capacity
#         self._A[self._front] = e
#         self._n += 1
#
#     def add_last(self, e):
#         if self._n == self._capacity:
#             self._resize(2 * self._capacity)
#         self._A[(self._front + self._n) % self._capacity] = e
#         self._n += 1
#
#     def delete_first(self):
#         if self.is_empty():
#             raise IndexError('덱이 비어있습니다')
#         tmp = self._A[self._front]
#         self._A[self._front] = None
#         self._front = (self._front + 1) % self._capacity
#         self._n -= 1
#         return tmp
#
#     def delete_last(self):
#         if self.is_empty():
#             raise IndexError('덱이 비어있습니다')
#         back = (self._front + self._n - 1) % self._capacity
#         tmp = self._A[back]
#         self._A[back] = None
#         self._n -= 1
#         return tmp
#
#     def _resize(self, capacity):
#         B = self._make_array(capacity)
#         for i in range(self._n):
#             B[i] = self._A[(self._front + i) % self._capacity]
#         self._A = B
#         self._front = 0
#         self._capacity = capacity
#
#     def __str__(self):
#         parts = []
#         for i in range(self._n):
#             parts.append(str(self._A[(self._front + i) % self._capacity]))
#         return '[' + ', '.join(parts) + ']'


if __name__ == '__main__':
    d = ArrayDeque()
    assert d.is_empty() is True
    assert len(d) == 0

    d.add_last(1); d.add_last(2); d.add_last(3)
    assert str(d) == '[1, 2, 3]'

    d.add_first(0)
    assert str(d) == '[0, 1, 2, 3]'
    assert d.first() == 0
    assert d.last() == 3
    assert len(d) == 4

    assert d.delete_first() == 0
    assert d.delete_last() == 3
    assert str(d) == '[1, 2]'

    # wrap-around + resize 확인
    d2 = ArrayDeque()
    for i in range(5):
        d2.add_first(i)                 # 4 3 2 1 0
    for i in range(10, 20):
        d2.add_last(i)
    expected = [4, 3, 2, 1, 0] + list(range(10, 20))
    assert [d2.delete_first() for _ in range(len(d2))] == expected
    assert d2.is_empty() is True

    # 빈 덱 예외 확인
    for fn in (d2.first, d2.last, d2.delete_first, d2.delete_last):
        try:
            fn()
            assert False, 'IndexError 가 발생해야 합니다'
        except IndexError:
            pass

    print('ArrayDeque 테스트 통과')
