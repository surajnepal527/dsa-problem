class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = []
        for s in strs:
            n = len(s)
            ch = "#"
            delimiter = str(n)+ch
            ans.append(delimiter)
            ans.append(s)
        return "".join(ans)
            



        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        n = len(s)
        ans = []
        cur,i = 0,0
        while i<n:
            while s[cur] != "#":
                cur += 1
            word_count = int(s[i:cur])
            ans.append(s[cur+1:cur+1+word_count])
            i = cur+1+word_count
            cur = i
        return ans
                



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))