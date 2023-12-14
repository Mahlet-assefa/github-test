class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0]*len(boxes)
        for direction in (lambda x:x, reversed):
            count = 0 
            move = 0
            for i in direction(range(len(boxes))):
                result[i] += move
                if boxes[i] == '1':
                    count += 1
                move += count
        return result