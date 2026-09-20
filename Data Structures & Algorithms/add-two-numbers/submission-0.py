# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy

        while l1 or l2 or carry: # edge case with only carry left
            l1_val = l1.val if l1 else 0 # edge case uneven length
            l2_val = l2.val if l2 else 0
            temp = l1_val + l2_val + carry # 6 + 6 + 0 = 12
            curr_val = temp % 10 # 12 // 10 = 1
            carry = temp // 10 # 12 % 10 = 2
            curr.next = ListNode(curr_val) # create the existing one!

            # move the pointers ahead
            l1 = l1.next if l1 else None # handling uneven cases
            l2 = l2.next if l2 else None 
            curr = curr.next

        return dummy.next


        