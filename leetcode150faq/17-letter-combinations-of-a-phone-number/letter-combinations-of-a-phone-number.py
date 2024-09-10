class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #ya jo backtrackign ka kahani ye aaj hi suru huwa hai
        #eek banda combinataion, perumation , all combination , find sets so on and so for..
        ## bol bol ke sataraha tha to mene boldia bhai backtracking karo bahi
        ## to bolta hai kase ro
        ## step1 Do somethign
        ## Explore 
        ## Remove step 1 and further explore

        #let do some prerequisite:
        num_map = { "2":  "abc", "3": "def", "4":"ghi", "5" : "jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        temp = []
        start_idx = 0
        if not digits:
            return []
        self.solve(start_idx, digits,num_map, temp, ans)
        return ans
    
    def solve(self, idx, digits,num_map, temp, ans):
        if idx >= len(digits):
            tmp_copy = temp[:]
            ans.append("".join(tmp_copy))
            return
        str = num_map[digits[idx]]
        for i in range (len(str)):
            temp.append(str[i])
            self.solve(idx+1, digits, num_map, temp, ans)
            temp.pop()
        


        