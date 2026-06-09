# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=head
        leftprev=dummy

        #find left ptr
        for i in range(left-1):
            leftprev=curr
            curr=curr.next
        #find r and reverse nodes from l to r
        #here curr is at l and lefttprev is at l-1
        prev=None
        for i in range(r-l+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        #now its reversed just need to connect this reversed list to main
        #list from both sides
        leftprev.next.next=curr
        leftprev.next=prev
        return dummy.next
