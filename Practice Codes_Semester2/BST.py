from LinkedBinaryTree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):

    def __init__(self,item=None,t_left=None,t_right=None):

        super().__init__(item,t_left,t_right)

    def insert(self,ele,pos):
        x=pos.item
        print(x)
        if ele==x:
            return 
        if ele<x:
            if pos.left is None:
                pos.left=self.addLeft(ele,pos)
            else:
                self.insert(ele,pos.left)
        if ele>x:
            if pos.right is None:
                pos.right=self.addRight(ele,pos)
            else:
                self.insert(ele,pos.right)
    
    def search(self,ele,pos):
        x=pos.item
        if ele==x:
            return pos
        elif ele<x:
            if pos.left is not None:
                self.search(ele,pos.left)
        elif ele>x:
            if pos.right is not None:
                self.search(ele,pos.right)
    
    def findMin(self,pos):
        pos=self.root
        if pos.left is not None:
            return self.findMin(pos.left)
        else:
            return pos

    def findMax(self,pos):
        pos=self.root
        if pos.right is not None:
            return self.findMax(pos.right)
        else:
            return pos

    def delete(self,item):
        pos=self.search(item,self.root)
        parent=pos.parent
        if self.num_children(pos)==0:
            if parent.left==pos:
                parent.left=None
            else:
                parent.right=None
        elif self.num_children(pos)==1:
            if parent.left is None and parent.right is not None:
                parent.right=pos.right
                pos.parent=pos.left=pos.right=None
                self.size-=1
            elif parent.right is None and parent.left is not None:
                parent.left=pos.left
                pos.parent=pos.left=pos.right=None
                self.size-=1
        elif self.num_children(pos)==2:
            r=self.findMin(pos.right)
            pos.item=r.item
            self.delete(r.item)
        
B=BinarySearchTree()
B.insert(20,B.root)
B.insert(30,B.root)
B.insert(35,B.root)
B.insert(40,B.root)
B.insert(73,B.root)
B.insert(23,B.root)
print(B)

x=B.search(23,B.root)
print(x)

k=B.findMax(B.root)
print(k.item)

B.delete(30)
print(B)


    
