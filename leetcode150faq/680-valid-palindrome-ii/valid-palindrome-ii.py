class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r=0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                l2,r2,l3,r3 = l+1,r,l,r-1
                #skip left
                left,right = True,True
                while l2<r2:
                    if s[l2] != s[r2]:
                        left = False
                        break
                    l2 += 1
                    r2 -= 1
                # skip right
                while l3<r3:
                    if s[l3] != s[r3]:
                        right = False
                        break
                    l3 += 1
                    r3 -=1
                if left == True or right == True:
                    return True
                    
                return False
            l += 1
            r -= 1
        return True
