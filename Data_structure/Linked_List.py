
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push_front(self, value):
        tmp = Node(value)
        tmp.next = self._head
        self._head = tmp
        self._size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        tmp = self._head.value
        self._head = self._head.next
        self._size -= 1
        return tmp

    def search(self,value):
        search_link = self._head
        while search_link:
            if value == search_link.value:
                return True
            else:
                search_link = search_link.next
        return False

    def __str__(self):
        search_link = self._head
        string = ""
        while search_link:
            string += str(search_link.value) +  " -> "
            search_link = search_link.next
        return string[:-4]



if __name__ == '__main__':
    L = SinglyLinkedList()
    print(L.is_empty())          # True
    L.push_front(3)
    L.push_front(2)
    L.push_front(1)
    print(L)                     # 1 -> 2 -> 3
    print(len(L))                # 3
    print(L.search(2), L.search(9))   # True False
    print(L.pop_front())         # 1
    print(L)                     # 2 -> 3