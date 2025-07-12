class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2

        self.map2=defaultdict(int)
        for i in self.nums2:
            self.map2[i]+=1
    

        

    def add(self, index: int, val: int) -> None:
        self.map2[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.map2[self.nums2[index]]+=1
        

    def count(self, tot: int) -> int:
        count=0
        for n1 in self.nums1:
            current=tot-n1
            if current in self.map2:
                count+=self.map2[current]
        return count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)