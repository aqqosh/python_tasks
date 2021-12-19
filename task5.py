from _typeshed import NoneType


def recursive(list1, list2, result):
    a = list1[0]
    b = list2[0]
    
    if len(list1) == 1:
        return [min([a, b]), max([a, b])]
    
    result = [min([a, b]), max([a, b])]
    return result + recursive(list1[1:], list2[1:], result)

list1 = [1, 2, 4, 7, 9, 10]
list2 = [1, 3, 4, 5, 8]

result = []
result = recursive(list1, list2, result)
result

### LINKED LIST

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

d1 = ListNode(val=9)
c1 = ListNode(val=6, next=d1)
b1 = ListNode(val=4, next=c1)
a1 = ListNode(val=3, next=b1)

d2 = ListNode(val=8)
c2 = ListNode(val=7, next=d2)
b2 = ListNode(val=3, next=c2)
a2 = ListNode(val=2, next=b2)
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        root = self.recursive(list1, list2)
        
        return root
    
    def recursive(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            
            return list2
    

sol = Solution()
res = sol.mergeTwoLists(a1, a2)