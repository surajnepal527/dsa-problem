class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        for i, num in enumerate(nums):
            if num in num_map:
                j = num_map[num]
                if abs(i-j) <= k:
                    return True
            num_map[num] = i
        return False

        