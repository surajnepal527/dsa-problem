class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        star_count = 0
        ans = []
        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                star_count += 1
            elif star_count > 0:
                star_count  -= 1
            else:
                ans.append(s[i])
        
        self.reverse(ans, 0, len(ans) - 1)
        return "".join(ans)


    
    def reverse(self, arr, start, end):
        while(start < end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


        