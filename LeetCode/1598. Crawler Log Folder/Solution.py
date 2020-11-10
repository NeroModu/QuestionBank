class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for op in logs:
            if op == '../':
                if count != 0:
                    count -= 1
            
            elif '/' in op and '.' not in op:
                count += 1
        
        return count
