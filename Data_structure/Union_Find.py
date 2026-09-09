"""
Union-Find (Disjoint Set, 서로소 집합)
원소들을 그룹으로 묶고, 두 원소가 같은 그룹인지 빠르게 확인한다.

두 가지 최적화가 핵심:
  - 경로 압축 (path compression): find 할 때 부모를 루트 쪽으로 당긴다
  - 크기 기준 합치기 (union by size): 작은 트리를 큰 트리 밑에 붙인다

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""


class UnionFind:
    def __init__(self, n):
        self._parent = list(range(n))   # 처음엔 각자 자기 자신이 루트
        self._size = [1] * n            # 각 루트가 거느린 원소 수
        self._count = n                 # 그룹 개수

    def find(self, x):
        # x 가 속한 그룹의 루트 반환 (경로 압축 적용)
        pass

    def union(self, x, y):
        # 합쳤으면 True, 이미 같은 그룹이면 False
        pass

    def connected(self, x, y):
        pass

    def count(self):
        # 남아있는 그룹 개수
        pass

    def size(self, x):
        # x 가 속한 그룹의 크기
        pass

    def groups(self):
        # {루트: [원소들]} 형태로 반환 (각 리스트는 정렬)
        pass


# ==================== 정답 ====================
# class UnionFind:
#     def __init__(self, n):
#         self._parent = list(range(n))
#         self._size = [1] * n
#         self._count = n
#
#     def find(self, x):
#         while self._parent[x] != x:
#             self._parent[x] = self._parent[self._parent[x]]   # 경로 압축
#             x = self._parent[x]
#         return x
#
#     def union(self, x, y):
#         rx, ry = self.find(x), self.find(y)
#         if rx == ry:
#             return False
#         if self._size[rx] < self._size[ry]:
#             rx, ry = ry, rx
#         self._parent[ry] = rx
#         self._size[rx] += self._size[ry]
#         self._count -= 1
#         return True
#
#     def connected(self, x, y):
#         return self.find(x) == self.find(y)
#
#     def count(self):
#         return self._count
#
#     def size(self, x):
#         return self._size[self.find(x)]
#
#     def groups(self):
#         out = {}
#         for x in range(len(self._parent)):
#             out.setdefault(self.find(x), []).append(x)
#         for root in out:
#             out[root].sort()
#         return out


if __name__ == '__main__':
    uf = UnionFind(10)
    assert uf.count() == 10
    assert uf.connected(0, 1) is False
    assert uf.size(0) == 1

    assert uf.union(0, 1) is True
    assert uf.union(1, 2) is True
    assert uf.connected(0, 2) is True
    assert uf.count() == 8
    assert uf.size(2) == 3

    # 이미 같은 그룹이면 False, 그룹 수도 그대로
    assert uf.union(0, 2) is False
    assert uf.count() == 8

    assert uf.union(3, 4) is True
    assert uf.union(4, 5) is True
    assert uf.connected(2, 3) is False

    # 두 덩어리 합치기
    assert uf.union(2, 5) is True
    assert uf.connected(0, 5) is True
    assert uf.size(0) == 6
    assert uf.count() == 5                 # {0..5}, {6}, {7}, {8}, {9}

    gs = uf.groups()
    assert len(gs) == 5
    assert sorted(gs.values()) == [[0, 1, 2, 3, 4, 5], [6], [7], [8], [9]]

    # 전부 하나로 합치기
    for i in range(9):
        uf.union(i, i + 1)
    assert uf.count() == 1
    assert uf.size(7) == 10
    assert list(uf.groups().values()) == [list(range(10))]

    # 큰 입력에서도 재귀 초과 없이 동작해야 함 (경로 압축 + 반복문)
    big = UnionFind(100000)
    for i in range(99999):
        big.union(i, i + 1)
    assert big.count() == 1
    assert big.connected(0, 99999) is True

    print('UnionFind 테스트 통과')
