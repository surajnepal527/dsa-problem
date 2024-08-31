class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        index = 0
        cur_char = chars[0]
        count = 1
        for i in range(1,len(chars)):
            if chars[i] == cur_char:
                count += 1
            else:
                chars[index] = cur_char
                index += 1
                if count > 1:
                    for c in str(count):
                        chars[index] = c
                        index += 1
                cur_char = chars[i]
                count = 1
                        
        chars[index] = cur_char
        index += 1
        if count > 1:
            for c in str(count):
                chars[index] = c
                index += 1

        return index
