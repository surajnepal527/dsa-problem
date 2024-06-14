class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #let do sorting first
        h_index = 0
        self.sort(0, len(citations) - 1, citations)
        for i in range (0, len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            #if i + 1 < len(citations) and citations[i] == citations[i + 1]:
              #  break
        return h_index
    
    def sort(self, start, end, A):
        if start >= end:
            return
        mid = (start + end) // 2
        self.sort(start, mid, A)
        self.sort(mid + 1, end , A)
        self.merge(start, mid, end, A)
    
    def merge(self,start, mid, end, A):
        left = A[start:mid+1]
        right= A[mid+ 1: end + 1]
        i = j = 0 
        k = start
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        

            

