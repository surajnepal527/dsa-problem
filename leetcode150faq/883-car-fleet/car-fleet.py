class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_list = [(position[i], speed[i]) for i in range(len(position))]
        pair_list_sorted = sorted(pair_list, key=lambda x:x[0])
        stack = []
        for r in range(len(position)- 1, -1,-1):
            duration = (target - pair_list_sorted[r][0])/pair_list_sorted[r][1]
            if not stack or duration > stack[-1]:
                stack.append(duration)
        
        return len(stack)
        