# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        newlist = None
        current = head

        while current:
            next_node = current.next
            current.next = newlist
            newlist = current
            current = next_node
        return newlist
        
