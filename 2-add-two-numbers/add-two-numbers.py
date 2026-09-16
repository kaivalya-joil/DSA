class Solution(object):
    def addTwoNumbers(self, l1, l2):

        temp1 = l1
        temp2 = l2

        rem = 0

        
        dummy = ListNode(0)
        current = dummy

        while temp1 != None or temp2 != None:

            if temp1 != None:
                x = temp1.val
            else:
                x = 0

            if temp2 != None:
                y = temp2.val
            else:
                y = 0

            total = x + y + rem

            digit = total % 10
            rem = total // 10

            
            current.next = ListNode(digit)
            current = current.next

            if temp1 != None:
                temp1 = temp1.next

            if temp2 != None:
                temp2 = temp2.next

        
        if rem > 0:
            current.next = ListNode(rem)

        return dummy.next