class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquare(n)
        power = 1
        lam = 1

        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            
            fast = self.sumOfSquare(fast)
            lam += 1
        
        if fast == 1: return True
        else: return False

    def sumOfSquare(self, n: int) -> int:
        output = 0

        while n:
            digit = n%10
            digit = digit ** 2
            output += digit
            n = n //10
        return output
