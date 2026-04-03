# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        
        prev = None
        curr = list1

        while curr and list2:
            if curr.val < list2.val:
                tmp = curr
                curr = curr.next
                prev = tmp
            
            else:
                tmp= list2.next
                if prev:
                    prev.next = list2
                else:
                    list2.next= curr
                    prev= list2
                    list1 = prev

                list2.next= curr
                prev= list2
                list2= tmp
        
        if list2:
            prev.next=list2


        
        return list1
