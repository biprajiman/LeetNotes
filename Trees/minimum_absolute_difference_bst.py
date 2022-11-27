"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference 
between the values of any two different nodes in the tree.
E.g.
      4
    /   \
   2     6
  / \      
 1   3

# Go through each node and find difference and track min
# inorder traversal

|1-2| |2-3| |4-1| |4-2| |4-3| |4-6|
difference between parent and all of its child

inorder traversal to get the list and get absolute distance from the list
keep track of parents and compare against all the values in the parents
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def get_min_distance(node: TreeNode, parents: List[TreeNode]):
    if len(parents) == 0:
        return float('inf')
    
    return min([abs(node.val - p.val) for p in parents])

def min_absolute_difference(node: TreeNode) -> int:
    parents = []
    def inorder(node:TreeNode, parents: List[TreeNode]):
        if not node:
            return float('inf')
        
        min_dist = get_min_distance(node, parents=parents)
        parents.append(node) # add me to parent
        left = inorder(node.left, parents)
        right = inorder(node.right, parents)
        parents.pop() # I am not parent anymore

        return min(min_dist, left, right)

    return inorder(node, parents)


if __name__ == '__main__':
    node = TreeNode