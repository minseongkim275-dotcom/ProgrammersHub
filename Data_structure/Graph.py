"""
Graph (그래프) - 인접 리스트 방식
{정점: [이웃, 이웃, ...]} 딕셔너리로 관리한다.

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""
from collections import deque


class Graph:
    def __init__(self, directed=False):
        self._adj = {}
        self._directed = directed

    def add_vertex(self, v):
        # 이미 있으면 아무것도 하지 않는다
        pass

    def add_edge(self, u, v):
        # 정점이 없으면 먼저 만들고 간선 추가
        # 무방향이면 양쪽 모두에 추가. 중복 간선은 넣지 않는다.
        pass

    def neighbors(self, v):
        # v 의 이웃 리스트 (없는 정점이면 빈 리스트)
        pass

    def vertices(self):
        pass

    def __len__(self):
        # 정점 개수
        pass

    def bfs(self, start):
        # 너비 우선 탐색 방문 순서 리스트. deque 사용
        pass

    def dfs(self, start):
        # 깊이 우선 탐색 방문 순서 리스트 (재귀)
        pass

    def dfs_iter(self, start):
        # 스택으로 구현한 DFS. 재귀 dfs 와 같은 순서가 나와야 한다.
        # 힌트: 이웃을 역순으로 스택에 넣는다
        pass

    def shortest_path(self, start, goal):
        # 간선 개수 기준 최단 경로 리스트, 못 가면 None
        # 힌트: BFS 하면서 prev[다음정점] = 현재정점 을 기록
        pass


# ==================== 정답 ====================
# class Graph:
#     def __init__(self, directed=False):
#         self._adj = {}
#         self._directed = directed
#
#     def add_vertex(self, v):
#         if v not in self._adj:
#             self._adj[v] = []
#
#     def add_edge(self, u, v):
#         self.add_vertex(u)
#         self.add_vertex(v)
#         if v not in self._adj[u]:
#             self._adj[u].append(v)
#         if not self._directed and u not in self._adj[v]:
#             self._adj[v].append(u)
#
#     def neighbors(self, v):
#         return list(self._adj.get(v, []))
#
#     def vertices(self):
#         return list(self._adj.keys())
#
#     def __len__(self):
#         return len(self._adj)
#
#     def bfs(self, start):
#         if start not in self._adj:
#             return []
#         visited = {start}
#         order = []
#         q = deque([start])
#         while q:
#             v = q.popleft()
#             order.append(v)
#             for w in self._adj[v]:
#                 if w not in visited:
#                     visited.add(w)
#                     q.append(w)
#         return order
#
#     def dfs(self, start):
#         if start not in self._adj:
#             return []
#         order = []
#         visited = set()
#
#         def rec(v):
#             visited.add(v)
#             order.append(v)
#             for w in self._adj[v]:
#                 if w not in visited:
#                     rec(w)
#
#         rec(start)
#         return order
#
#     def dfs_iter(self, start):
#         if start not in self._adj:
#             return []
#         order = []
#         visited = set()
#         stack = [start]
#         while stack:
#             v = stack.pop()
#             if v in visited:
#                 continue
#             visited.add(v)
#             order.append(v)
#             for w in reversed(self._adj[v]):
#                 if w not in visited:
#                     stack.append(w)
#         return order
#
#     def shortest_path(self, start, goal):
#         if start not in self._adj or goal not in self._adj:
#             return None
#         prev = {start: None}
#         q = deque([start])
#         while q:
#             v = q.popleft()
#             if v == goal:
#                 path = []
#                 while v is not None:
#                     path.append(v)
#                     v = prev[v]
#                 return path[::-1]
#             for w in self._adj[v]:
#                 if w not in prev:
#                     prev[w] = v
#                     q.append(w)
#         return None


if __name__ == '__main__':
    #  A - B
    #  |   |
    #  C - D - E        F (외톨이)
    g = Graph()
    for u, v in [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]:
        g.add_edge(u, v)
    g.add_vertex('F')

    assert len(g) == 6
    assert sorted(g.vertices()) == ['A', 'B', 'C', 'D', 'E', 'F']
    assert g.neighbors('A') == ['B', 'C']
    assert g.neighbors('D') == ['B', 'C', 'E']
    assert g.neighbors('없는정점') == []

    # 중복 간선은 무시
    g.add_edge('A', 'B')
    assert g.neighbors('A') == ['B', 'C']

    assert g.bfs('A') == ['A', 'B', 'C', 'D', 'E']
    assert g.dfs('A') == ['A', 'B', 'D', 'C', 'E']
    assert g.dfs_iter('A') == g.dfs('A')
    assert g.bfs('F') == ['F']

    assert g.shortest_path('A', 'E') == ['A', 'B', 'D', 'E']
    assert g.shortest_path('A', 'A') == ['A']
    assert g.shortest_path('A', 'F') is None
    assert g.shortest_path('A', '없는정점') is None

    # 방향 그래프
    dg = Graph(directed=True)
    dg.add_edge('A', 'B')
    dg.add_edge('B', 'C')
    assert dg.neighbors('A') == ['B']
    assert dg.neighbors('B') == ['C']
    assert dg.bfs('A') == ['A', 'B', 'C']
    assert dg.bfs('C') == ['C']
    assert dg.shortest_path('C', 'A') is None

    print('Graph 테스트 통과')
