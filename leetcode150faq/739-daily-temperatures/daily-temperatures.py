class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = []
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                ans[i] = 0
            else:
                ans[i] =  stack[-1] - i
            stack.append(i)
        
        return ans
            
