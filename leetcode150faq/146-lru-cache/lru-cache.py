class Node:
    def __init__(self, key=0, val=0,next=None, prev=None):
        self.key=key
        self.val=val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head , self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveNodeToHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveNodeToHead(node)
        else:
            if len(self.cache) == self.cap:
                self.removeLRUNode()
            newNode = Node(key=key, val=value)
            self.cache[key] = newNode
            self.addNodeToHead(newNode)

    
    def removeNode(self, node):
        node_next, node_prev = node.next, node.prev
        node.prev.next, node.next.prev = node_next, node_prev

    def removeLRUNode(self):
        lru = self.tail.prev
        self.removeNode(lru)
        del self.cache[lru.key]

    def addNodeToHead(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node    

    def moveNodeToHead(self, node):
        self.removeNode(node)
        self.addNodeToHead(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)