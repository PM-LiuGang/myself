import unittest

# 7-5 7-6
# 单向列表实现栈
class Empty(Exception):
    pass


class LinkedStack:

    #--------nested_Node class------------
    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------stack methods------------------

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self.Node(e, self._head) # Node._next -> self._head
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._head._element

    def pop(self):
        # 从栈的顶部移除元素，并显示移除的元素 LIFO
        if self.is_empty():
            raise Empty('Stack is empty.')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


# 7-6 7-7
# 单向链表实现队列
class LinkedQueue:
    # FIFO

    #--------nested_Node class------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------stack methods------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._head._element

    # myself
    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._tail._element

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None  # 适配队列在没移除元素，只有一个元素
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest  # _next不是已经指向了newest了么？
        self._size += 1


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    #--------nested_Node class------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------stack methods------------------

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next  # circularly
            self._tail._next = newest  # 旧尾连接新头
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


# 712 双向列表的基本类
class _DoublyLinkedBase:

    class _Node:

        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            """

            :param element: object
            :param prev: _Node ?
            :param next: _Node ?
            """
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """
        prev | header | next -> prev | trailer | next
                             <-
        """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """

        :param e:
        :param predecessor: _Node
        :param successor:  _Node
        :return:  _Node
        """
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest  # ?
        successor._prev = newest  # ?
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev # 记录删除目标节点的引用
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


# 713
class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._delete_node(self._trailer._prev)


#714
class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""
    class Position:
        """实例化后表示列表中元素的位置”“”"""
        def __init__(self, container, node):
            """
            Constructor should not be invoked by user.

            :param container: ?
            :param node:
            """
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and \
                   other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    #---utility method-------------------------------
    def _validate(self, p):
        """
        返回给定位置的节点
        :param p: Position
        :return:  指定位置对应的节点
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type.')
        if p._container is not self:
            raise ValueError('p dose not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is no longer valid.')
        return p._node
    #----utility method--------------------------------

    def _make_position(self, node):
        """
        返回指定节点对应的位置
        :param node: 节点
        :return: 节点位置
        """
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    #---accessors-------------------------------------
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    #---multators--------------------------------------

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


#717
def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and\
                        L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


#718
class FavoritesList:

    #-----------nested _Item class---------------
    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0

    #---------------nopublic utilties-------------
    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and \
                        cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    #-------------------public methods--------------------
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Ilegal Value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)


class FavoritestListMTF(FavoritesList):

    def _move_up(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k.')
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        for j in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)


#TestCase
class TestLinked(unittest.TestCase):

    def test_linkedStack_push(self):
        ls = LinkedStack()
        for i in 'liugang':
            ls.push(i)
        self.assertEqual(ls.top(), 'g')

    def test_LinkedStack_pop(self):
        ls = LinkedStack()
        for i in 'liugang':
            ls.push(i)
        ls.pop()
        ls.pop()
        self.assertEqual(ls.pop(), 'a')

    def test_linkedQueue_en(self):
        lq = LinkedQueue()
        for i in 'liugang':
            lq.enqueue(i)
        self.assertEqual(lq.first(), 'l')

    def test_linkedQueue_de(self):
        lq = LinkedQueue()
        for i in 'liugang':
            lq.enqueue(i)
        lq.dequeue()
        lq.dequeue()
        self.assertEqual(lq.first(), 'u')

    def test_CircularQueue(self):
        cq = CircularQueue()
        for i in 'liugang':
            cq.enqueue(i)
        cq.dequeue()
        cq.dequeue()
        self.assertEqual(cq.first(), 'u')

    def test_CircularQueue(self):
        cq = CircularQueue()
        for i in 'liugang':
            cq.enqueue(i)
        cq.dequeue()
        cq.dequeue()
        cq.rotate()
        self.assertEqual(cq.first(), 'g')

    def test_LinkedQueue(self):
        lq = LinkedDeque()
        lq.insert_first('liu')
        lq.insert_first('gang')
        lq.insert_last('end')
        lq.delete_first()
        self.assertEqual(lq.first(), 'liu')

    def test_deleteNode(self):
        lq = LinkedDeque()
        lq.insert_first('gang')
        lq.insert_last('end')
        lq.insert_last('end-liu')
        lq.delete_last()
        self.assertEqual(lq.last(), 'end')

    def test_PositionList(self):
        pl = PositionalList()
        pl.add_first('l')
        pl.add_last('g')
        pl.add_after(1,'add_after') # error
        pl.add_before(1, 'add_before') # error
        self.assertEqual((pl.first()).element(), 'l')

if __name__ == '__main__':
    unittest.main()