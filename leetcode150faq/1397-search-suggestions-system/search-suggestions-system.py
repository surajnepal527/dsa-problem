class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        #first we are going to sort our product list
        products.sort() # nlogn + m*
        # we have our two pointer
        ans = []
        left, right = 0, len(products) - 1
        for i in range(len(searchWord)):
            while left <= right and (len(products[left]) <= i or products[left][i] != searchWord[i]):
                left += 1
            
            while left <= right and (len(products[right]) <= i or products[right][i] != searchWord[i]):
                right -= 1
            
            rem = right - left +1
            ans.append([])
            for j in range(min(3, rem)):
                ans[-1].append(products[left+j])
        
        return ans



                






