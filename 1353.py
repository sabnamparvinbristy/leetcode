class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        maxNum=max(i for a, i in events)
        events.sort()

        ans=0
        b=[]
        k=0

        for j in range(1,maxNum+1):
            while k<len(events) and events [k][0]==j:
                heapq.heappush(b,events[k][1])
                k=k+1
            while b and j> b[0]:
                heapq.heappop(b)
            if b and j<=b[0]:
                heapq.heappop(b)
                ans=ans+1
            if not b and k==len(events):
                break
        return ans

        
        