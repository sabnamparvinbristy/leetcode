from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts=Counter(arr)
        maximum=0

        for i in arr:
            if counts[i]==i:
                maximum=max(maximum,i)

        if maximum==0:
            return -1
        else:
            return maximum
        