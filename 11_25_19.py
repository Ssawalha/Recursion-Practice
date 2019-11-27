class Node: 
    def __init__(self, num, next):
        self.num = num
        self.next = next
    
    def recursive_len(self):
        if self.next == None:
            return 1
        else:
            return 1 + self.next.len()

# TIME COMPLEXITY:
# it is O of n ( can we skip any of the elements, or going over anything twice. (answer for both is No so we can assume it is O of N))

# how do we make it be O of 1 or constant run time?

class NodeConstant:
    def __init__(self, num, next): 
        self.num = num
        self.next = next
        if next == None: #AMORTIZE
            self.count = 1
        else: 
            self.count = 1 + self.next.count
    
    def len(self):
        return self.count


#TREES

# a tree is either:
# [] (empty)
# or 
# (num, left, right)
# where num is an integer and left & right are both trees

# Defining a tree in python:

class TreeNode: #binary tree
    def __init__(self, num, left, right):
        self.num = num
        self.left = left
        self.right = right


        if self.left == None and self.right == None:
            self.count = 1
        elif self.left != None and self.right != None:
            self.count = 1  + self.left.count + self.right.count
        elif self.left != None and self.right == None:
            self.count = 1 + self.left.count
        elif self.left == None and self.right != None:
            self.count = 1 + self.right.count

    def recursive_len(self):
        if self == None:
            return 0
        elif self.left == None and self.right == None:
            return 1
        else:
            return 1 + self.left.len() + self.right.len()
    
    def o_1_count(self):
        return self.count

    def search(self, target): # for a binary search tree
        if self == None:
            return False
        elif self.num == target:
            return True
        elif self.num > target:
            return self.left.search(target)
        elif self.num > target and self.left == None:
            return False
        elif self.num < target and self.right == None:
            return False
        else:
            return self.right.search(target)

    def altsearch(self, target):
        if self == None:
            return False
        if self.num == target:
            return True
        else:
            return self.left.search() or self.right.search()
#Binary search tree:
# O(log n) because we wouldnt search the left side if target is larger than self.num