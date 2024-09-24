class Node:
    def __init__(self, key=0, prev= None, next = None,val = 0):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self._moveToHead(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self._moveToHead(node)
        else:
            if self.size == self.capacity:
                self._removeLRUNode()
            new_node = Node(key=key, val=value)
            self.hm[key] = new_node
            self._addNodeToHead(new_node)
            self.size += 1 

    def _moveToHead(self, node):
        self._removeNode(node)
        self._addNodeToHead(node)
        
    def _removeNode(self, node):
        node_prev = node.prev
        node_next = node.next
        node.prev.next = node_next
        node.next.prev = node_prev
    
    def _addNodeToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _removeLRUNode(self):
        lru_node = self.tail.prev
        self._removeNode(lru_node)
        del self.hm[lru_node.key]
        self.size -= 1

    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)