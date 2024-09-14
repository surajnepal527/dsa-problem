class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        ans = []
        isInserted = [False] * n
        i = 0
        while i < n:
            if not isInserted[i]:
                cur_ans = []
                cur_ans.append(strs[i])
                isInserted[i] = True
                cur_hm = {}
                for idx, ch in enumerate(strs[i]):
                    cur_hm[ch] = cur_hm.get(ch,0) + 1
                #check for rest of the array if there is any anagram
                if i + 1 < n:
                    for j in range(i+1, n):
                        if not isInserted[j] and len(strs[i]) == len(strs[j]):
                            next_hm = {}
                            for idx, ch in enumerate(strs[j]):
                                next_hm[ch] = next_hm.get(ch, 0)+1
                            #now check for anagram from two hash map
                            isValid = True
                            for ch_key in next_hm:
                                if ch_key not in cur_hm or cur_hm[ch_key] != next_hm[ch_key]:
                                    isValid = False
                                    break
                            if isValid:
                                cur_ans.append(strs[j])
                                isInserted[j] = True
                ans.append(cur_ans)
            i += 1
        return ans
    

                        


        