# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        ans=""
        while(temp):
            ans+=str(temp.val)
            temp=temp.next
        return(int(ans,2))
        