# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        slow.next = prev

        # Compare the first half with the reversed second half
        left = head
        right = slow.next
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
        

        