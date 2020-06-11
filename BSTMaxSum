# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    
    def maxSumBST(self, root: TreeNode) -> int:
        self.SumTree(root)
        return self.res
        
        

        
        
    def SumTree(self, root):
        if not root:
            return True, 0
        
        lbst, sumLeft = self.SumTree(root.left)
        rbst, sumRight = self.SumTree(root.right)
        isBST, treeSum = True, root.val + sumLeft + sumRight
        if not lbst or not rbst:
            return False, 0
        
        if lbst and rbst:
            if root.left and root.val <= root.left.val:
                isBST = False
            if root.right and root.val >= root.right.val:
                isBST = False
            if isBST:
                self.res = max(self.res, treeSum)
        print(root.val)
        return isBST, treeSum 
        
        
        
    def GetHeight(self, node):
        if node is None: 
            return 0 
        else : 
            # Compute the height of each subtree  
            rheight = self.GetHeight(node.right) 
            lheight = self.GetHeight(node.left) 

            #Use the larger one 
            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1
            
            
    def rootLevel(self, root, level):
        if not root:
            return None
        
        if level == 1:
            self.SumTree(root)
        elif level > 1 : 
            self.rootLevel(root.left , level-1) 
            self.rootLevel(root.right , level-1) 
        
        
        
        
