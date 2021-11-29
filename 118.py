# my first

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            res = [[1],[1,1]]
            
            for i in range(3,numRows+1):
                r = []
                for j in range(i):
                    if j == 0 or j == i-1:
                        r.append(1)
                    else:
                        r.append(res[i-2][j]+res[i-2][j-1])
                        
                res.append(r)
            return res



# better

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]*(i+1) for i in range(numRows)]
        for i in range(1,numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j]+res[i-1][j-1]
        return res



# Accept my knees

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            res += [list(map(lambda x,y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]