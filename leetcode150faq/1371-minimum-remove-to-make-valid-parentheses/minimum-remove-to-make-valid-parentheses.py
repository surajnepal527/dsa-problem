class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        spc = 0
        epc= 0
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                ans.append(s[i])
            else:
                if s[i] == '(':
                    spc += 1
                    ans.append(s[i])
                elif s[i] == ')' and spc > epc:
                    epc += 1
                    ans.append(s[i])
                else:
                    continue
        
        if spc == epc:
            return ''.join(ans)
        else:
            nans = []
            nspc = 0
            nepc = 0
            for i in range(len(ans)-1, -1, -1):
                if ans[i] != '(' and ans[i] != ')':
                    nans.append(ans[i])
                else:
                    if ans[i] == ')':
                        nepc += 1
                        nans.append(ans[i])
                    elif ans[i] == '(' and nspc < nepc:
                        nspc += 1
                        nans.append(ans[i])
                    else:
                        continue
            return ''.join(reversed(nans))
            # fans = []
            # for i in range(len(nans)-1, -1, -1):
            #     fans.append(nans[i])
            
            # return ''.join(fans)


