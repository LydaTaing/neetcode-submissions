class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = 0,0,0
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[2] > target[2] or triplet[1] > target[1]:
                continue
            x = max(x, triplet[0])
            y = max(y, triplet[1])
            z = max(z, triplet[2])
            if x == target[0] and y == target[1] and z == target[2]:
                return True
        return False