
# my

from functools import lru_cache
class Solution:
    @lru_cache
    def tribonacci(self, n: int) -> int:
        x0 , x1, x2 = 0, 1, 1
        if n == 0:
            return 0
        elif n==1 or n==2:
            return 1
        return self.tribonacci(n-3)+ self.tribonacci(n-2) + self.tribonacci(n-1)
		
# optimal

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        a,b,c = 0,1,1
        for _ in range(n-2):
            a,b,c = b,c, a+b+c
        return c