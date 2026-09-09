"""
Binary Search Tree (이진 탐색 트리)
왼쪽 서브트리 < 노드 < 오른쪽 서브트리

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        pass

    def is_empty(self):
        pass

    def insert(self, key, value=None):
        # 같은 key 가 이미 있으면 value 만 갱신 (size 증가 X)
        pass

    def search(self, key):
        # 해당 key 의 Node 반환, 없으면 None
        pass

    def __contains__(self, key):
        pass

    def min(self):
        # 가장 작은 key / 비었으면 IndexError
        pass

    def max(self):
        # 가장 큰 key / 비었으면 IndexError
        pass

    def delete(self, key):
        # 삭제 성공하면 True, key 가 없으면 False
        # 힌트: 자식 0개 / 1개 / 2개 세 경우로 나눈다.
        #       자식 2개면 오른쪽 서브트리의 최솟값(중위 후속자)으로 대체
        pass

    def inorder(self):
        # 중위 순회 key 리스트 (오름차순이 나와야 정상)
        pass

    def preorder(self):
        # 전위 순회 key 리스트
        pass

    def postorder(self):
        # 후위 순회 key 리스트
        pass

    def level_order(self):
        # 레벨(너비) 순회 key 리스트
        pass

    def height(self):
        # 트리 높이. 빈 트리는 -1, 루트만 있으면 0
        pass


# ==================== 정답 ====================
# class Node:
#     def __init__(self, key, value=None):
#         self.key = key
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self._root = None
#         self._size = 0
#
#     def __len__(self):
#         return self._size
#
#     def is_empty(self):
#         return self._size == 0
#
#     def insert(self, key, value=None):
#         if self._root is None:
#             self._root = Node(key, value)
#             self._size += 1
#             return
#         cur = self._root
#         while True:
#             if key == cur.key:
#                 cur.value = value
#                 return
#             elif key < cur.key:
#                 if cur.left is None:
#                     cur.left = Node(key, value)
#                     self._size += 1
#                     return
#                 cur = cur.left
#             else:
#                 if cur.right is None:
#                     cur.right = Node(key, value)
#                     self._size += 1
#                     return
#                 cur = cur.right
#
#     def search(self, key):
#         cur = self._root
#         while cur is not None:
#             if key == cur.key:
#                 return cur
#             cur = cur.left if key < cur.key else cur.right
#         return None
#
#     def __contains__(self, key):
#         return self.search(key) is not None
#
#     def min(self):
#         if self._root is None:
#             raise IndexError('트리가 비어있습니다')
#         cur = self._root
#         while cur.left is not None:
#             cur = cur.left
#         return cur.key
#
#     def max(self):
#         if self._root is None:
#             raise IndexError('트리가 비어있습니다')
#         cur = self._root
#         while cur.right is not None:
#             cur = cur.right
#         return cur.key
#
#     def delete(self, key):
#         if self.search(key) is None:
#             return False
#         self._root = self._delete(self._root, key)
#         self._size -= 1
#         return True
#
#     def _delete(self, node, key):
#         if node is None:
#             return None
#         if key < node.key:
#             node.left = self._delete(node.left, key)
#         elif key > node.key:
#             node.right = self._delete(node.right, key)
#         else:
#             if node.left is None:
#                 return node.right
#             if node.right is None:
#                 return node.left
#             succ = node.right
#             while succ.left is not None:
#                 succ = succ.left
#             node.key, node.value = succ.key, succ.value
#             node.right = self._delete(node.right, succ.key)
#         return node
#
#     def inorder(self):
#         out = []
#
#         def rec(node):
#             if node is None:
#                 return
#             rec(node.left)
#             out.append(node.key)
#             rec(node.right)
#
#         rec(self._root)
#         return out
#
#     def preorder(self):
#         out = []
#
#         def rec(node):
#             if node is None:
#                 return
#             out.append(node.key)
#             rec(node.left)
#             rec(node.right)
#
#         rec(self._root)
#         return out
#
#     def postorder(self):
#         out = []
#
#         def rec(node):
#             if node is None:
#                 return
#             rec(node.left)
#             rec(node.right)
#             out.append(node.key)
#
#         rec(self._root)
#         return out
#
#     def level_order(self):
#         if self._root is None:
#             return []
#         out = []
#         q = [self._root]
#         while q:
#             node = q.pop(0)
#             out.append(node.key)
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         return out
#
#     def height(self):
#         def rec(node):
#             if node is None:
#                 return -1
#             return 1 + max(rec(node.left), rec(node.right))
#
#         return rec(self._root)


if __name__ == '__main__':
    t = BinarySearchTree()
    assert t.is_empty() is True
    assert t.height() == -1

    #         50
    #      30     70
    #    20  40 60  80
    for k in [50, 30, 70, 20, 40, 60, 80]:
        t.insert(k, str(k))

    assert len(t) == 7
    assert t.inorder() == [20, 30, 40, 50, 60, 70, 80]
    assert t.preorder() == [50, 30, 20, 40, 70, 60, 80]
    assert t.postorder() == [20, 40, 30, 60, 80, 70, 50]
    assert t.level_order() == [50, 30, 70, 20, 40, 60, 80]
    assert t.height() == 2
    assert t.min() == 20 and t.max() == 80

    assert (40 in t) is True
    assert (99 in t) is False
    assert t.search(40).value == '40'

    # 중복 insert 는 value 만 갱신
    t.insert(40, 'forty')
    assert len(t) == 7
    assert t.search(40).value == 'forty'

    # 자식 0개 삭제
    assert t.delete(20) is True
    assert t.inorder() == [30, 40, 50, 60, 70, 80]
    assert len(t) == 6

    # 자식 1개 삭제 (30 -> 40 이 올라옴)
    assert t.delete(30) is True
    assert t.inorder() == [40, 50, 60, 70, 80]

    # 자식 2개 삭제 (루트)
    assert t.delete(50) is True
    assert t.inorder() == [40, 60, 70, 80]
    assert len(t) == 4

    # 없는 키
    assert t.delete(12345) is False
    assert len(t) == 4

    empty = BinarySearchTree()
    for fn in (empty.min, empty.max):
        try:
            fn()
            assert False, 'IndexError 가 발생해야 합니다'
        except IndexError:
            pass

    print('BinarySearchTree 테스트 통과')
