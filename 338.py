# Approach Best

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(1,n+1):
            res[i] = res[i>>1] + i%2
        return res
    


# Approach 2

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if i == offset*2:
                offset *= 2
            res[i] = res[i-offset] + 1
        return res
		
# Brute Force


class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            arr.append(str(bin(i)).count('1'))
        
        return arr
    