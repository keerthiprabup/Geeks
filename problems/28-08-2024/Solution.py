class Solution:
    def countNodesInLoop(self, head):
        if head is None:
            return 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return 0
            
        loop_length = 0
        current = slow
        while True:
            current = current.next
            loop_length += 1
            if current == slow:
                break
        
        return loop_length
