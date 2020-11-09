class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        
        neg = False
        if x < 0:
            neg = True
            x *= -1
            
        while x > 0:
            a = x % 10
            rev = rev * 10 + a
            x = x // 10
            
        if abs(rev) > 2 ** 31 - 1:
            return 0
        
        return rev if not neg else rev * -1
