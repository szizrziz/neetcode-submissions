# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        movingdummy=dummy
        while list1 and list2:
            if list1.val<list2.val:
                movingdummy.next=list1
                list1=list1.next
            else:
                movingdummy.next=list2
                list2=list2.next
            movingdummy=movingdummy.next
        if list1:
            movingdummy.next=list1
        elif list2:
            movingdummy.next=list2
        return dummy.next
        
            


        