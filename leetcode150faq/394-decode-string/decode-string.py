class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            #append all the character to stack till we found the closing square braces
            if char != "]":
                stack.append(char)
            # when we found the closing square braces instead of inserting 
            #we need to start poping and do computation as follow
            else:
                #lets first declare a sub string to collect the character that need be
                #repeated
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring

                #we need to do one more pop for staring square braces
                stack.pop()
                #now lets process the digit
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                #now we are going to append the substring back to stack
                stack.append(int(k) * substring)

        return "".join(stack)

