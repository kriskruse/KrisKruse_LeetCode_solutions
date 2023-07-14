# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""  # 342
        str2 = ""  # 465
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        str3 = str(int(str1[::-1]) + int(str2[::-1]))[::-1]
        l3 = ListNode(int(str3[-1]))
        for i in range(len(str3) - 2, -1, -1):
            l3 = ListNode(int(str3[i]), l3)
        return l3


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    ln = Solution().addTwoNumbers(l1, l2)
    strout = ""
    while ln:
        strout += str(ln.val)
        ln = ln.next
    print(strout)

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    ln = Solution().addTwoNumbers(l1, l2)
    strout = ""
    while ln:
        strout += str(ln.val)
        ln = ln.next
    print(strout)
