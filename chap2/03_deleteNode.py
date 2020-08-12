class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next==None:   #要删除的节点为尾节点
            node=None
        else:                 #要删除的节点为中间节点
            node.val=node.next.val
            node.next=node.next.next