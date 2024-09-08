from collections import defaultdict
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        #create adjaceny list
        #run dfs
        #if it going away from parent and path is real 
        adj_list = defaultdict(list)
        for u, v in connections:
            adj_list[u].append([v,1])
            adj_list[v].append([u,0])
        count = [0]
        self.dfs(0, -1, adj_list, count)
        return count[0]
        
    
    def dfs(self, source, parent, adj_list, count):
        for pair in adj_list[source]:
            v = pair[0]
            check = pair[1]
            if v != parent:
                if check == 1:
                    count[0] += 1
                self.dfs(v,source,adj_list, count)
        



        