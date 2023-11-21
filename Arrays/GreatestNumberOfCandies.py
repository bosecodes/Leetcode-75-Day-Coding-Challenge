class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for b in candies:
            if(b+ extraCandies >= max(candies)):
                res.append(True)
            else:
                res.append(False)
        return res
