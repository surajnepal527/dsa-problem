class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < 1 or len(haystack) < len(needle):
            return -1
        j = 0
        for i in range(0, len(haystack)):
            end = i + len(needle)
            k = 0
            if end <= len(haystack):
                for j in range(i, end):
                    if haystack[j] == needle[k]:
                        if k == len(needle) - 1:
                            return i
                        k += 1
                    else:
                        break

        return -1        