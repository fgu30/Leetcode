class Node:
    
    def __init__(self,key = 0,val = 0):
        self.key = key
        self.val = val
        self.prev  = None
        self.next = None
        
class LRUCache:
    
    def __init__(self,capacity):
        self.size = capacity
        self.hashmap = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_last(self,node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        
        
    def delete_the_fist(self,node):
        self.removeNode(node)
        self.move_to_last(node)
        
        
    
    
    def get(self,key):
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.delete_the_fist(node)
        return node.val
        
        
    def put(self,key,value):
        if  key in self.hashmap:
            
            node = self.hashmap[key] 
            node.val = value
            self.delete_the_fist(node)
            return
        if len(self.hashmap) == self.size:
            del self.hashmap[self.head.next.key]
            self.removeNode(self.head.next)
        node = Node(key,value)
        self.hashmap[key] = node
        self.move_to_last(node)
        
            
            
        