from absbt import AbstractBinaryTree

class LinkedBT:

    class BTNode:

        def __init__(self,item=None,left=None,right=None,parent=None):

            self.item=item
            self.left=left
            self.right=right
            self.parent=parent
        
        def __getitem__(self):
            return self.item
        
        def __setitem__(self,item):
            self.item=item
    
    def __init__(self,item,left=None,right=None,parent=None):

        self.root=None
        self.size=0
        if item is not None:
            self.root=self.addRoot(item)
        if left is not None:
            if left.root is not None:
                left.root.parent=self.root
                self.root.left=left.root
                self.size+=left.size
                left.root=None
                left.size=0

        if right is not None:
            if right.root is not None:
                right.root.parent=self.root
                self.root.right=right.root
                self.size+=right.size
                right.root=None
                right.size=0
    
    def root(self):
        return self.root
    
    def left(self,pos):
        if pos.isleaf():
            return ValueError
        if pos.left is None:
            return ValueError
        return pos.left
    
    def right(self,pos):
        if pos.isleaf():
            return ValueError
        if pos.right is None:
            return ValueError
        return pos.right
    
    def addRoot(self,item):

        if self.root is not None:
            return ValueError
        self.root=LinkedBT.BTNode(item)
        self.size+=1
    
    def __str__(self):

        def inorder(pos):
            out=""
            if pos.left is not None:
                out+=inorder(pos.left)
            if pos.right is not None:
                out+=inorder(pos.right)
            return out
        return inorder(self.root)

T=LinkedBT(1)
print(T)


    



