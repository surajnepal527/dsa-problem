import heapq
class Solution(object):

    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # Greedy Algorithm , we want to maximize both nums1 choice and also maximize min value from nums2
        #1. sort nums2 in descending order sort we try to pick max value for min 
        #2. to remove the min value from nums1 as we proceed we will use min heap.

        #lets first do the merge sort to solve this problem for sorting
        n = len(nums1)
        min_heap = []
        max_sum = 0
        cur_sum = 0
        count = 0
        self.mergeSort(nums1, nums2, 0, n-1)
        for i in range(n):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums1[i])
                cur_sum += nums1[i]
                if k-1 == i:
                    max_sum = cur_sum * nums2[i]
            else:
                cur_sum +=  nums1[i] - heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums1[i])
                max_sum = max(max_sum, cur_sum * nums2[i])
        
        return max_sum
                







    def mergeSort(self, nums1, nums2, start ,end):
        if start >=  end:
            return
        mid = (start + end) // 2
        self.mergeSort(nums1, nums2, start, mid)
        self.mergeSort(nums1, nums2, mid+1, end)
        self.merge(nums1, nums2,start, mid, end)
    
    def merge(self, nums1, nums2, start, mid, end):
        left2 = nums2[start:mid+1]
        right2= nums2[mid+1:end+1]
        left1 = nums1[start:mid+1]
        right1 = nums1[mid+1:end+1]
        i = j = 0
        k = start
        while i < len(left2) and j < len(right2):
            if left2[i] >= right2[j]:
                nums2[k] = left2[i]
                nums1[k] =  left1[i]
                i += 1
            else:
                nums2[k] = right2[j]
                nums1[k] = right1[j]
                j += 1
            k += 1
        
        while i < len(left2):
            nums2[k] = left2[i]
            nums1[k] = left1[i]
            i += 1
            k += 1
        while j < len(right2):
            nums2[k] = right2[j]
            nums1[k] = right1[j]
            j += 1
            k += 1
            



        