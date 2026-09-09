"""
Trie (트라이) - 문자열 접두사 트리
각 노드가 {문자: 자식노드} 딕셔너리를 갖는다.
단어의 마지막 글자 노드에 is_end = True 를 표시한다.

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self._root = TrieNode()
        self._size = 0

    def __len__(self):
        # 저장된 단어 개수
        pass

    def insert(self, word):
        # 이미 있는 단어면 size 증가 X
        pass

    def _find_node(self, prefix):
        # prefix 를 따라간 마지막 노드 반환, 경로가 없으면 None
        pass

    def search(self, word):
        # 정확히 그 단어가 저장돼 있으면 True
        pass

    def starts_with(self, prefix):
        # 그 접두사로 시작하는 단어가 하나라도 있으면 True
        pass

    def __contains__(self, word):
        pass

    def words_with_prefix(self, prefix):
        # 접두사로 시작하는 모든 단어 (정렬해서 반환)
        pass

    def delete(self, word):
        # 삭제 성공하면 True, 없는 단어면 False
        # 힌트: 재귀로 내려갔다 올라오면서, 자식도 없고 단어 끝도 아닌
        #       노드는 부모에서 제거한다
        pass


# ==================== 정답 ====================
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
#
#
# class Trie:
#     def __init__(self):
#         self._root = TrieNode()
#         self._size = 0
#
#     def __len__(self):
#         return self._size
#
#     def insert(self, word):
#         cur = self._root
#         for ch in word:
#             if ch not in cur.children:
#                 cur.children[ch] = TrieNode()
#             cur = cur.children[ch]
#         if not cur.is_end:
#             cur.is_end = True
#             self._size += 1
#
#     def _find_node(self, prefix):
#         cur = self._root
#         for ch in prefix:
#             if ch not in cur.children:
#                 return None
#             cur = cur.children[ch]
#         return cur
#
#     def search(self, word):
#         node = self._find_node(word)
#         return node is not None and node.is_end
#
#     def starts_with(self, prefix):
#         return self._find_node(prefix) is not None
#
#     def __contains__(self, word):
#         return self.search(word)
#
#     def words_with_prefix(self, prefix):
#         node = self._find_node(prefix)
#         if node is None:
#             return []
#         out = []
#
#         def collect(node, path):
#             if node.is_end:
#                 out.append(path)
#             for ch, child in node.children.items():
#                 collect(child, path + ch)
#
#         collect(node, prefix)
#         return sorted(out)
#
#     def delete(self, word):
#         if not self.search(word):
#             return False
#         self._delete(self._root, word, 0)
#         self._size -= 1
#         return True
#
#     def _delete(self, node, word, depth):
#         # 반환값: 이 노드를 부모에서 지워도 되는가
#         if depth == len(word):
#             node.is_end = False
#             return len(node.children) == 0
#         ch = word[depth]
#         child = node.children[ch]
#         if self._delete(child, word, depth + 1):
#             del node.children[ch]
#             return (not node.is_end) and len(node.children) == 0
#         return False


if __name__ == '__main__':
    t = Trie()
    assert len(t) == 0
    assert t.search('cat') is False
    assert t.starts_with('c') is False
    assert t.words_with_prefix('c') == []

    for w in ['cat', 'car', 'card', 'care', 'dog', 'do']:
        t.insert(w)
    assert len(t) == 6

    assert t.search('cat') is True
    assert t.search('ca') is False          # 접두사일 뿐 단어는 아님
    assert t.search('cards') is False
    assert ('do' in t) is True

    assert t.starts_with('ca') is True
    assert t.starts_with('card') is True
    assert t.starts_with('z') is False

    assert t.words_with_prefix('car') == ['car', 'card', 'care']
    assert t.words_with_prefix('do') == ['do', 'dog']
    assert t.words_with_prefix('') == ['car', 'card', 'care', 'cat', 'do', 'dog']

    # 중복 insert 는 개수가 늘지 않음
    t.insert('cat')
    assert len(t) == 6

    # 다른 단어의 접두사인 단어 삭제 -> 나머지는 살아있어야 함
    assert t.delete('car') is True
    assert len(t) == 5
    assert t.search('car') is False
    assert t.search('card') is True
    assert t.search('care') is True

    # 잎 노드 삭제
    assert t.delete('card') is True
    assert t.search('care') is True
    assert t.words_with_prefix('ca') == ['care', 'cat']

    # 없는 단어
    assert t.delete('없는단어') is False
    assert t.delete('ca') is False
    assert len(t) == 4

    # 한글도 동작
    k = Trie()
    k.insert('가나다')
    k.insert('가나')
    assert k.words_with_prefix('가') == ['가나', '가나다']

    print('Trie 테스트 통과')
