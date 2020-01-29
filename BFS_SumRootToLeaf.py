# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:07:03 2020

@author: WELCOME
"""
"""
Sum Root to leaf Solution
BFS
Working on Leetcode
Time complexity= O(N)
Spece Complexity = O(N)
"""

class binaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
from collections import deque
class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        queue=deque()
        queue.append((root,0))
        result=0
        while queue:
            size=len(queue)
            for i in range(size):
                currNode=queue.popleft()
                if currNode[0].left:                   queue.append([currNode[0].left,currNode[1]*10+currNode[0].val])
                if currNode[0].right:                   queue.append([currNode[0].right,currNode[1]*10+currNode[0].val])
                if not currNode[0].left and not currNode[0].right:
                    tempResult=currNode[1]*10+currNode[0].val
                    result=result+tempResult
        return result

treeNode=binaryTree(6)
treeNode.left=binaryTree(4)
treeNode.right=binaryTree(8)
treeNode.left.left=binaryTree(1)
print(Solution().sumNumbers(treeNode))