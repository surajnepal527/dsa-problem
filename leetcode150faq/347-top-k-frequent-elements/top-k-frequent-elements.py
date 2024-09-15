class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = [[] for _ in range(len(nums)+1)] 
        ans = []
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
            tmp[freq].append(num)
        
        for i in range(len(nums), -1, -1):
            for num in tmp[i]:
                if k > 0:
                    ans.append(num)
                    k -= 1
                else:
                    return ans
        return ans

