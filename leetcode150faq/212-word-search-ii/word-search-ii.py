class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True
        
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        for w in words:
            self.root.addWord(w)
            
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(row, col, node, word):
            
            if (row == rows or col == cols or row < 0 or col < 0 or board[row][col] not in node.children or (row, col) in visit):
                return
         
            visit.add((row,col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.endOfWord:
                res.add(word)
            dfs(row-1,col, node, word)
            dfs(row+1,col, node, word)
            dfs(row,col-1, node, word)
            dfs(row,col+1, node, word)
            visit.remove((row, col))
          
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, self.root,"") 

        return list(res)
    

    
    


        