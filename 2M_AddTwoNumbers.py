# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        output = None
        fin  = None
        carry = 0
        while t1!=None and t2!=None:
            if output == None:
                output = ListNode(0, None)
                fin = output
            else:
                output.next = ListNode(0, None)
                output = output.next
            sum = t1.val+t2.val+carry
            output.val = sum%10
            if sum >=10:
                carry = int(sum/10)
            else:
                carry = 0
            t1 = t1.next
            t2 = t2.next


            
        while t1!=None:
            output.next = ListNode(0, None)
            output = output.next
            sum = t1.val+carry
            output.val = sum%10
            if sum >=10:
                carry = int(sum/10)
            else:
                carry = 0
            t1 = t1.next

        while t2!=None:
            output.next = ListNode(0, None)
            output = output.next
            sum = t2.val+carry
            output.val = sum%10
            if sum >=10:
                carry = int(sum/10)
            else:
                carry = 0
            t2 = t2.next
        
        if carry>0:
            output.next = ListNode(carry, None)
            output = output.next
        
        return fin