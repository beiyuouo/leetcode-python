# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/14 01:17
# Description:

__author__ = "BeiYu"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = ListNode()
        even_head = ListNode()

        q, oh, eh = head, odd_head, even_head
        idx = 1
        while q is not None:
            if idx % 2 == 1:
                oh.next = q
                oh = oh.next
            else:
                eh.next = q
                eh = eh.next

            # print(q.val)
            q = q.next
            idx = idx + 1

        oh.next = even_head.next
        eh.next = None
        return odd_head.next


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    head = ListNode()
    hq = head
    for i in range(len(a) - 1):
        hq.val = a[i]
        hq.next = ListNode()
        hq = hq.next
    hq.val = a[-1]
    head_ = Solution().oddEvenList(head)
    print('ok')

    import time

    # time.sleep(10)
    while head_:
        print(head_.val)
        head_ = head_.next
