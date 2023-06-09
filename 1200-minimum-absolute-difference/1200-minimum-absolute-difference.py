class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        Diff = [arr[i+1] - arr[i] for i in range (len(arr)-1)]
        target = min(Diff)
        res = []
        for i,j in enumerate(Diff):
            if j == target:
                res.append([arr[i], arr[i+1]])
        return res