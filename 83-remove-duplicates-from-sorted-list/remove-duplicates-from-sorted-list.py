# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return
            
        map = []
        tmp = head

        map.append(tmp.val)
        
        while tmp and tmp.next:
            if tmp.next.val not in map:
                map.append(tmp.next.val)
                tmp = tmp.next
            else:
                tmp.next = tmp.next.next      
        return head
        