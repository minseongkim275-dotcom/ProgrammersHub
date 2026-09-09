"""
Min Heap (최소 힙) - 리스트 기반 완전이진트리
부모 <= 자식. 루트가 항상 최솟값.

인덱스 규칙 (0-based)
  부모 = (i - 1) // 2
  왼쪽 = 2 * i + 1
  오른쪽 = 2 * i + 2

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""


class MinHeap:
    def __init__(self, items=None):
        self._A = list(items) if items else []
        if self._A:
            self._heapify()

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def __len__(self):
        pass

    def is_empty(self):
        pass

    def peek(self):
        # 최솟값 확인 (제거 X) / 비었으면 IndexError
        pass

    def push(self, x):
        # 맨 뒤에 넣고 위로 올린다
        pass

    def pop(self):
        # 루트를 꺼내고, 마지막 원소를 루트로 올린 뒤 아래로 내린다
        # 비었으면 IndexError
        pass

    def _sift_up(self, i):
        # i 가 부모보다 작으면 계속 교환
        pass

    def _sift_down(self, i):
        # 두 자식 중 더 작은 쪽과 비교해서 계속 교환
        pass

    def _heapify(self):
        # 임의의 리스트를 힙으로 만든다. O(n)
        # 힌트: 마지막 부모부터 0번까지 거꾸로 _sift_down
        pass


def heap_sort(items):
    # MinHeap 을 이용해 오름차순 정렬된 리스트 반환
    pass


# ==================== 정답 ====================
# class MinHeap:
#     def __init__(self, items=None):
#         self._A = list(items) if items else []
#         if self._A:
#             self._heapify()
#
#     def _parent(self, i):
#         return (i - 1) // 2
#
#     def _left(self, i):
#         return 2 * i + 1
#
#     def _right(self, i):
#         return 2 * i + 2
#
#     def __len__(self):
#         return len(self._A)
#
#     def is_empty(self):
#         return len(self._A) == 0
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError('힙이 비어있습니다')
#         return self._A[0]
#
#     def push(self, x):
#         self._A.append(x)
#         self._sift_up(len(self._A) - 1)
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError('힙이 비어있습니다')
#         top = self._A[0]
#         last = self._A.pop()
#         if self._A:
#             self._A[0] = last
#             self._sift_down(0)
#         return top
#
#     def _sift_up(self, i):
#         while i > 0:
#             p = self._parent(i)
#             if self._A[i] < self._A[p]:
#                 self._A[i], self._A[p] = self._A[p], self._A[i]
#                 i = p
#             else:
#                 break
#
#     def _sift_down(self, i):
#         n = len(self._A)
#         while True:
#             l, r = self._left(i), self._right(i)
#             smallest = i
#             if l < n and self._A[l] < self._A[smallest]:
#                 smallest = l
#             if r < n and self._A[r] < self._A[smallest]:
#                 smallest = r
#             if smallest == i:
#                 break
#             self._A[i], self._A[smallest] = self._A[smallest], self._A[i]
#             i = smallest
#
#     def _heapify(self):
#         for i in range(self._parent(len(self._A) - 1), -1, -1):
#             self._sift_down(i)
#
#
# def heap_sort(items):
#     h = MinHeap(items)
#     return [h.pop() for _ in range(len(h))]


if __name__ == '__main__':
    h = MinHeap()
    assert h.is_empty() is True

    for x in [5, 3, 8, 1, 9, 2]:
        h.push(x)

    assert len(h) == 6
    assert h.peek() == 1
    assert len(h) == 6                      # peek 은 제거하지 않음

    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 3
    assert len(h) == 3

    # 힙 속성 유지 확인
    rest = [h.pop() for _ in range(len(h))]
    assert rest == [5, 8, 9]
    assert h.is_empty() is True

    # 리스트로 한 번에 힙 만들기 (_heapify)
    h2 = MinHeap([7, 2, 9, 4, 1, 8, 3])
    assert h2.peek() == 1
    assert [h2.pop() for _ in range(len(h2))] == [1, 2, 3, 4, 7, 8, 9]

    # 우선순위 큐로 쓰기 (튜플 비교)
    pq = MinHeap()
    pq.push((2, '보통'))
    pq.push((1, '급함'))
    pq.push((3, '나중에'))
    assert pq.pop() == (1, '급함')
    assert pq.pop() == (2, '보통')

    assert heap_sort([5, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 4, 5, 5, 6, 9]
    assert heap_sort([]) == []

    empty = MinHeap()
    for fn in (empty.peek, empty.pop):
        try:
            fn()
            assert False, 'IndexError 가 발생해야 합니다'
        except IndexError:
            pass

    print('MinHeap 테스트 통과')
