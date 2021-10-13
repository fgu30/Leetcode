class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 0
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    def append(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def pop_first(self) -> Node:
        if self.head.next == self.tail:
            return None
        return self.remove(self.head.next)

    def is_empty(self) -> bool:
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_to_node_list = collections.defaultdict(DLinkedList)
        self.key_to_node = {}
        self.min_freq = 0

    def __pop_least_freq(self):
        removed_node = self.freq_to_node_list[self.min_freq].pop_first()
        del self.key_to_node[removed_node.key]
        if self.freq_to_node_list[self.min_freq].is_empty():
            del self.freq_to_node_list[removed_node.freq]
            # we update min_freq after exiting this function in put()

    def __use(self, node):
        # remove the node from its current position
        self.freq_to_node_list[node.freq].remove(node)
        if self.freq_to_node_list[node.freq].is_empty():
            del self.freq_to_node_list[node.freq]
            if self.min_freq == node.freq:
                self.min_freq += 1
        # insert the node to its new position
        node.freq += 1
        self.freq_to_node_list[node.freq].append(node)

    def get(self, key: int) -> int:
        try:
            node = self.key_to_node[key]
        except KeyError:
            return -1
        self.__use(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        try:
            # node already in cache, update node
            node = self.key_to_node[key]
            node.val = value
            self.__use(node)
        except KeyError:
            # new node
            node = Node(key=key, val=value)
            self.freq_to_node_list[node.freq].append(node)
            self.key_to_node[key] = node
            # pop the least frequently used node if exceeds capacity
            if len(self.key_to_node) > self.capacity:
                self.__pop_least_freq()
            self.min_freq = min(0, self.min_freq)
