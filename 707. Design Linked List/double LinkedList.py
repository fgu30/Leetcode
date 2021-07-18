class Node:
    def __init__(self, x: int):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = Node(0)
        self._tail = Node(0)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._length = 0

    def getByIndex(self, index: int):
        """
        通过index获取节点
        """
        if index < 0 or index > self._length - 1:
            return None
        if index  <= (self._length - 1) // 2:
            cur = self._head
            for i in range(index + 1):
                cur = cur.next
        else:
            cur = self._tail
            for i in range(self._length - index):
                cur = cur.prev
        return cur

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        res = self.getByIndex(index)
        if res:
            return res.val
        else:
            return -1

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """

        newNode = Node(val)
        # 生成新节点

        newNode.next = self._head.next
        newNode.prev = self._head
        # 新节点属性改变,next为原先的节点,prev为头结点
        self._head.next.prev = newNode
        self._head.next = newNode
        # 头结点指向新节点

        self._length += 1

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        # 生成新节点

        newNode.prev = self._tail.prev
        newNode.next = self._tail
        # 新节点属性改变,next为尾结点,prev为插入节点
        self._tail.prev.next = newNode
        self._tail.prev = newNode
        # 头结点指向新节点
        self._length += 1

    def addAtIndex(self, index: int, val: int) :
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        # 判断index的值,调用上面的接口完成插入
        if index > self._length:
            return
        if index < 0:
            return self.addAtHead(val)
        if index == self._length:
            return self.addAtTail(val)

        # 生成新节点
        newNode = Node(val)
        # 获取原索引节点
        node = self.getByIndex(index)
        prev = node.prev
        # 插入节点
        prev.next = newNode
        newNode.prev = prev
        node.prev = newNode
        newNode.next = node

        self._length += 1

    def deleteAtIndex(self, index: int) :
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.getByIndex(index)
        if node:
            prev = node.prev
            nextNode = node.next
            prev.next = nextNode
            nextNode.prev = prev
            self._length -= 1
