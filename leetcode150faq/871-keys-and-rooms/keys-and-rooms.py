class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        source = 0
        self.depthFirstSearch(rooms,source, visited)
        for v in visited:
            if not v:
                return False
        
        return True
        
    
    def depthFirstSearch(self, rooms, source, visited):
        visited[source] = True

        for node in rooms[source]:
            if not visited[node]:
                self.depthFirstSearch(rooms, node, visited)
        