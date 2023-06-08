from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        res,  sortedList = deque(),  SortedList()
        for num in nums[::-1]:
            res.appendleft(sortedList.bisect_left(num))
            sortedList.add(num)
        return res