# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            res=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                res.append(self.merge(l1,l2))
            lists=res
        return lists[0]
    def merge(self,list1,list2):
        dummy=ListNode()
        moving=dummy
        while list1 and list2:
            if list1.val<list2.val:
                moving.next=list1
                list1=list1.next
            else:
                moving.next=list2
                list2=list2.next
            moving=moving.next
        if list1:
            moving.next=list1
        elif list2:
            moving.next=list2
        return dummy.next