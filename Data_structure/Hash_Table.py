"""
Hash Table (해시 테이블) - 체이닝(chaining) 방식
각 버킷에 (key, value) 튜플 리스트를 두고 충돌을 처리한다.

부하율(load factor)이 0.75 를 넘으면 용량을 2배로 늘린다.

아래 pass 를 지우고 직접 구현해보세요.
정답은 파일 아래쪽에 주석으로 있습니다.
"""


class HashTable:
    DEFAULT_CAPACITY = 8
    LOAD_FACTOR = 0.75

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self._capacity = capacity
        self._buckets = [[] for _ in range(self._capacity)]
        self._n = 0

    def _hash(self, key):
        # 파이썬 내장 hash() 를 쓰고 용량으로 나눈 나머지
        pass

    def __len__(self):
        pass

    def put(self, key, value):
        # 이미 있는 key 면 값만 갱신, 없으면 추가
        # 추가 후 부하율 초과하면 _resize(2 * capacity)
        pass

    def get(self, key):
        # 값 반환 / 없으면 KeyError
        pass

    def remove(self, key):
        # 삭제 후 값 반환 / 없으면 KeyError
        pass

    def __contains__(self, key):
        pass

    def keys(self):
        # 모든 key 리스트
        pass

    def items(self):
        # 모든 (key, value) 리스트
        pass

    def _resize(self, capacity):
        # 새 버킷 배열을 만들고 전부 다시 해싱해서 넣는다
        pass

    # 아래 두 개는 위 메서드가 완성되면 자동으로 동작합니다.
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


# ==================== 정답 ====================
# class HashTable:
#     DEFAULT_CAPACITY = 8
#     LOAD_FACTOR = 0.75
#
#     def __init__(self, capacity=DEFAULT_CAPACITY):
#         self._capacity = capacity
#         self._buckets = [[] for _ in range(self._capacity)]
#         self._n = 0
#
#     def _hash(self, key):
#         return hash(key) % self._capacity
#
#     def __len__(self):
#         return self._n
#
#     def put(self, key, value):
#         bucket = self._buckets[self._hash(key)]
#         for i, (k, _) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 return
#         bucket.append((key, value))
#         self._n += 1
#         if self._n > self._capacity * self.LOAD_FACTOR:
#             self._resize(2 * self._capacity)
#
#     def get(self, key):
#         bucket = self._buckets[self._hash(key)]
#         for k, v in bucket:
#             if k == key:
#                 return v
#         raise KeyError(key)
#
#     def remove(self, key):
#         bucket = self._buckets[self._hash(key)]
#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 self._n -= 1
#                 return v
#         raise KeyError(key)
#
#     def __contains__(self, key):
#         bucket = self._buckets[self._hash(key)]
#         return any(k == key for k, _ in bucket)
#
#     def keys(self):
#         return [k for bucket in self._buckets for k, _ in bucket]
#
#     def items(self):
#         return [(k, v) for bucket in self._buckets for k, v in bucket]
#
#     def _resize(self, capacity):
#         old = self.items()
#         self._capacity = capacity
#         self._buckets = [[] for _ in range(capacity)]
#         self._n = 0
#         for k, v in old:
#             self.put(k, v)
#
#     def __getitem__(self, key):
#         return self.get(key)
#
#     def __setitem__(self, key, value):
#         self.put(key, value)


if __name__ == '__main__':
    h = HashTable()
    assert len(h) == 0

    h.put('apple', 1)
    h.put('banana', 2)
    h.put('cherry', 3)
    assert len(h) == 3
    assert h.get('banana') == 2
    assert ('apple' in h) is True
    assert ('durian' in h) is False

    # 덮어쓰기는 개수가 늘지 않음
    h.put('apple', 100)
    assert len(h) == 3
    assert h.get('apple') == 100

    # 대괄호 문법
    h['grape'] = 4
    assert h['grape'] == 4
    assert len(h) == 4

    assert h.remove('banana') == 2
    assert len(h) == 3
    assert ('banana' in h) is False

    # 없는 키는 KeyError
    for fn in (lambda: h.get('banana'), lambda: h.remove('banana')):
        try:
            fn()
            assert False, 'KeyError 가 발생해야 합니다'
        except KeyError:
            pass

    # 리사이즈 후에도 전부 살아있어야 함
    big = HashTable()
    for i in range(100):
        big.put('key%d' % i, i * i)
    assert len(big) == 100
    assert big._capacity > 8
    assert sorted(big.keys()) == sorted('key%d' % i for i in range(100))
    for i in range(100):
        assert big.get('key%d' % i) == i * i

    # 문자열 말고 다른 타입 키도 동작
    mixed = HashTable()
    mixed.put(1, 'one')
    mixed.put((2, 3), 'tuple')
    assert mixed.get(1) == 'one'
    assert mixed.get((2, 3)) == 'tuple'
    assert sorted(mixed.items(), key=str) == sorted([(1, 'one'), ((2, 3), 'tuple')], key=str)

    print('HashTable 테스트 통과')
