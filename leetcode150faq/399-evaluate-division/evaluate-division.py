from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj_list = defaultdict(list)
        for index, variables in enumerate(equations):
            src = variables[0]
            des = variables[1]
            val = values[index] 
            adj_list[src].append([des, val])
            adj_list[des].append([src, 1/val])
        
        ans = [-1.0] * len(queries)
        res = 1
        for i , (u, v)  in enumerate(queries):
            if u not in adj_list or v not in adj_list:
                continue

            visited = self.setVisited(adj_list)
            res = self.dfs(u, v, adj_list,visited, 1.0)
            if res != -1.0:
                ans[i] = res
        
        return ans
    
    def dfs(self, src, des, adj_list, visited, res):
        if src == des:
            return res

        visited[src] = True

        for neig,val in adj_list[src]:
            if not visited[neig]:
                result = self.dfs(neig,des, adj_list, visited, res * val)
                if result != -1.0: # Only return if a valid path was found
                    return result
            
        return -1.0 # If no valid path found, return -1.0
        
    def setVisited(self, adj_list):
        return {node:False for node in adj_list}





        