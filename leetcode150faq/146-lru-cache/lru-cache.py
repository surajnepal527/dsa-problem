class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #remove from existing location
            self.insert(self.cache[key]) # add to the right most position
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
            
        
    def remove(self ,node:Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def insert(self, node:Node):
        prev , next = self.right.prev , self.right
        prev.next = next.prev = node
        node.next , node.prev = next, prev

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)