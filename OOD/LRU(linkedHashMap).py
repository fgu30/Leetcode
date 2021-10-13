

'''
move_to_end(last= True-default): to the right of the arr
popitem(last = True): the right of  the arr

'''

from collections import OrderedDict

class LRUCache:
    
    def __init__(self,capacity):
        self.OD = OrderedDict()
        self.size = capacity
        
    def get(self,key):
        if key in self.OD:
            self.OD.move_to_end(key)
            return self.OD[key]
        else:
            return -1
    def put(self,key,value):
        self.OD[key] = value
        if key in self.OD:
            self.OD.move_to_end(key)

        if len(self.OD) > self.size: 
            self.OD.popitem(last=False)


            
             
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)