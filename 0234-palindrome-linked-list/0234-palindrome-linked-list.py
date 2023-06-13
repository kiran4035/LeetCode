# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        x = head # present node
        while x is not None:
            arr.append(x.val)
            x = x.next
        return arr == arr[::-1]

        