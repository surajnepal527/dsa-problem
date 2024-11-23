class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquare(n)
            if n == 1: return True
        return False
    def sumOfSquare(self, n:int) -> int:
        result = 0
        while n:
            digit = n%10
            digit = digit ** 2
            result += digit
            n = n // 10
        return result

        
        