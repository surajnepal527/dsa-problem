class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for f, t in tickets:
            adj[f].append(t)
        for f in adj:
            adj[f].sort(reverse=True)
        
        res = []

        def dfs(airport):
            while adj[airport]:
                next_dest = adj[airport].pop()
                dfs(next_dest)
            res.append(airport)
        dfs("JFK")
        return res[::-1]
        