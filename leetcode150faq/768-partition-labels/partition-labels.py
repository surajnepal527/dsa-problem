class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lst_idx_map = {}
        result = []
        for i, ch in enumerate(s):
            lst_idx_map[ch] = i
        size, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, lst_idx_map[ch])
            size += 1
            if end == i:
                result.append(size)
                size = 0
        return result

            
            

        



        