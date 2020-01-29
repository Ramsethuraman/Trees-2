# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:07:03 2020

@author: WELCOME
"""
"""
Sum Root to leaf Solution
DFS
Working on Leetcode
Time complexity= O(N)
Space Complexity = O(H) 
"""

class binaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        result=0
        def sumNums(root,result):
            #Base
            if root==None:
                return 0
            if root.left==None and root.right==None:
                return result*10+root.val
            
            #Logic
            case1=sumNums(root.left,result*10+root.val)
            case2=sumNums(root.right,result*10+root.val)
            return case1+case2
        return sumNums(root,0)

treeNode=binaryTree(6)
treeNode.left=binaryTree(4)
treeNode.right=binaryTree(8)
treeNode.left.left=binaryTree(1)
print(Solution().sumNumbers(treeNode))