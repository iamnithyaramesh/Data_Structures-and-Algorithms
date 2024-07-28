
from absbt import AbstractBinaryTree

class LinkedBT:

    class LinkedNode:

        __slots__=['item','left','right','parent']

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

        if (item is not None):
            self.addRoot(item)
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
    
    def addRoot(self,item):
        if item is None:
            return ValueError
        self.root=self.LinkedNode(item)
        self.size+=1

    def addLeft(self,item,pos):
        if pos is None:
            return TypeError
        if pos.left is not None:
            return ValueError
        pos.left=self.LinkedNode(item)
        self.size+=1

    def addRight(self,item,pos):
        if pos is None:
            return TypeError
        if pos.right is not None:
            return ValueError
        pos.right=self.LinkedNode(item)
        self.size+=1
    
    def __str__(self):

        def preorder(pos):
            res=f"[{pos.item}"
            if pos.left is not None:
             res+=preorder(pos.left)
            if  pos.right is not None:
             res+=preorder(pos.right)
            res+="]"
            return res
        return preorder(self.root)

    def parent(self,pos):
        if pos.parent is None:
            return ValueError
        return self.parent(pos)


