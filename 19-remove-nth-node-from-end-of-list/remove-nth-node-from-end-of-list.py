class Solution(object):
    def removeNthFromEnd(self, head, n):

        count = 1
        temp = head

        while temp.next != None:
            temp = temp.next
            count += 1

        if n == count:
            return head.next

        r = count - n

        temp = head

        for i in range(r - 1):
            temp = temp.next

        temp.next = temp.next.next

        return head

        

