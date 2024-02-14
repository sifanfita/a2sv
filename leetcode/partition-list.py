# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_x = ListNode()
        greater_than_or_equal_to_x = ListNode()
        less_than_x_head = less_than_x
        greater_than_or_equal_to_x_head = greater_than_or_equal_to_x

        current = head
        while current:
            if current.val < x:
                less_than_x.next = current
                less_than_x = less_than_x.next
            else:
                greater_than_or_equal_to_x.next = current
                greater_than_or_equal_to_x = greater_than_or_equal_to_x.next
            current = current.next

       
        less_than_x.next = greater_than_or_equal_to_x_head.next
        greater_than_or_equal_to_x.next = None
        return less_than_x_head.next
       

        
        

            

        