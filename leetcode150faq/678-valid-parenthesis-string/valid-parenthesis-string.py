class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        openstk = []
        askstk = []
        for i in range(n):
            if s[i] == "(":
                openstk.append(i)
            elif s[i] == "*":
                askstk.append(i)
            else:
                if openstk:
                    openstk.pop()
                elif askstk:
                    askstk.pop()
                else:
                    return False
        
        while openstk and askstk:
            if openstk[-1] > askstk[-1]: return False
            openstk.pop()
            askstk.pop()
        return True if not openstk else False
                

        