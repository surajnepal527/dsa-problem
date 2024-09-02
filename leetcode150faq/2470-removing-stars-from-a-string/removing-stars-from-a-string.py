class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        star_count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                star_count += 1
            elif star_count > 0:
                star_count -= 1
            else:
                arr.append(s[i])
        
        ans = []
        while arr:
            ans.append(arr.pop())
        
        return "".join(ans)
                

        