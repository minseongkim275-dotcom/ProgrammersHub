"""
Doubly Linked List (이중 연결 리스트) - 양쪽 더미 노드 방식
head, tail 더미 덕분에 경계 처리(빈 리스트/첫 노드/끝 노드)를 따로 안 해도 된다.

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""



class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self._head = Node()          # 더미
        self._tail = Node()          # 더미
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_before(self, node, value):
        # node 바로 앞에 새 노드를 끼워넣고, 그 새 노드를 반환
        # 힌트: prev = node.prev 를 잡아두고 링크 4개를 다시 건다
        pass

    def _delete(self, node):
        # node 를 떼어내고 값을 반환 (더미는 들어오지 않는다고 가정)
        pass

    def push_front(self, v):
        self._insert_before(self._head.next, v)

    def push_back(self, v):
        self._insert_before(self._tail, v)

    def pop_front(self):
        if self.is_empty():
            raise IndexError('비어있습니다')
        return self._delete(self._head.next)

    def pop_back(self):
        if self.is_empty():
            raise IndexError('비어있습니다')
        return self._delete(self._tail.prev)

    def __str__(self):
        parts = []
        cur = self._head.next
        while cur is not self._tail:
            parts.append(str(cur.value))
            cur = cur.next
        return ' <-> '.join(parts)


# ==================== 정답 ====================
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.prev = None
#         self.next = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self._head = Node()
#         self._tail = Node()
#         self._head.next = self._tail
#         self._tail.prev = self._head
#         self._size = 0
#
#     def __len__(self):
#         return self._size
#
#     def is_empty(self):
#         return self._size == 0
#
#     def _insert_before(self, node, value):
#         prev = node.prev
#         new = Node(value)
#         new.prev = prev
#         new.next = node
#         prev.next = new
#         node.prev = new
#         self._size += 1
#         return new
#
#     def _delete(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         node.prev = node.next = None
#         self._size -= 1
#         return node.value
#
#     def push_front(self, v):
#         self._insert_before(self._head.next, v)
#
#     def push_back(self, v):
#         self._insert_before(self._tail, v)
#
#     def pop_front(self):
#         if self.is_empty():
#             raise IndexError('비어있습니다')
#         return self._delete(self._head.next)
#
#     def pop_back(self):
#         if self.is_empty():
#             raise IndexError('비어있습니다')
#         return self._delete(self._tail.prev)
#
#     def __str__(self):
#         parts = []
#         cur = self._head.next
#         while cur is not self._tail:
#             parts.append(str(cur.value))
#             cur = cur.next
#         return ' <-> '.join(parts)


if __name__ == '__main__':
    d = DoublyLinkedList()
    assert d.is_empty() is True
    assert len(d) == 0
    assert str(d) == ''

    d.push_back(2); d.push_back(3)
    d.push_front(1)
    assert str(d) == '1 <-> 2 <-> 3'
    assert len(d) == 3

    assert d.pop_back() == 3
    assert d.pop_front() == 1
    assert str(d) == '2'
    assert len(d) == 1

    assert d.pop_back() == 2
    assert d.is_empty() is True
    assert str(d) == ''

    # 다 비운 뒤에도 다시 넣을 수 있어야 함 (링크가 안 망가졌는지)
    d.push_front('a'); d.push_back('b')
    assert str(d) == 'a <-> b'

    # 빈 리스트 예외
    e = DoublyLinkedList()
    for fn in (e.pop_front, e.pop_back):
        try:
            fn()
            assert False, 'IndexError 가 발생해야 합니다'
        except IndexError:
            pass

    print('DoublyLinkedList 테스트 통과')