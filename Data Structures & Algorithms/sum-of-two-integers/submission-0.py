class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 01 +01 = 10
        # XOR then shift the carry and add 

        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF

        while b != 0:
            carry = (a&b)<< 1
            a = (a ^ b) & mask
            b = carry & mask
        
        if a <= maxInt:
            return a
        else:
            return ~(a^mask)
