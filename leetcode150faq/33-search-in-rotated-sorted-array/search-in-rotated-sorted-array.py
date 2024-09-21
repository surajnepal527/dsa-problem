import sys
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_val = sys.maxsize
        left, right = 0 , len(nums) - 1
        min_idx = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < min_val:
                min_idx = mid
                min_val = nums[mid]
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        
        left_arr = nums[0:min_idx]
        right_arr = nums[min_idx:len(nums)]
        left_left = 0 
        left_right = len(left_arr) -1
        while left_left <= left_right:
            left_mid = (left_left+left_right)//2
            if left_arr[left_mid] > target:
                left_right = left_mid - 1
            elif left_arr[left_mid] < target:
                left_left = left_mid + 1
            else:
                return left_mid
        
        right_left = 0
        right_right = len(right_arr) -1
        while right_left <= right_right:
            right_mid = (right_left + right_right)//2
            if right_arr[right_mid] < target:
                right_left = right_mid + 1
            elif right_arr[right_mid] > target:
                right_right = right_mid - 1
            else:
                return right_mid+min_idx
        
        return -1