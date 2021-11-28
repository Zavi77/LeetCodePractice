# Brute force

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        final = []
        
        for i in range(len(boxes)):
            res = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    res += abs(i-j)
        
            final.append(res)
        return final
		
# Optimal

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        final = [0]*len(boxes)
        leftcost, rightcost, leftcount, rightcount = 0, 0, 0, 0
        for i in range(1,len(boxes)):
            if boxes[i-1] == '1':
                leftcount += 1
            leftcost += leftcount
            final[i] += leftcost
        for i in range(len(boxes)-2,-1,-1):
            if boxes[i+1] == '1':
                rightcount += 1
            rightcost += rightcount
            final[i] += rightcost
        return final