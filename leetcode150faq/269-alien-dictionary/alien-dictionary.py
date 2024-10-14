class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c : set() for word in words for c in word }
        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            #w1=apes and w2=ape -> this in not valid as per question
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = set()
        cur_path = set()
        res = []
        def dfs(c):
            if c in cur_path:
                return True
            if c in visited:
                return False
            cur_path.add(c)
            for nei in adj[c]:
                if dfs(nei) : return True
            visited.add(c)
            cur_path.remove(c)
            res.append(c)
        for c in adj:
            if dfs(c): return ""
        res.reverse()
        return "".join(res)



        