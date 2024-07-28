from abc import ABC,abstractmethod

class AbstractTree:
   
   
   ''' Member Functions: 

   Abstract Methods: root()
                    parent()
                    children()
                    num_children()
                    __len__()

Concrete Methods : isroot()

                   heightN()
                   height()

'''

# Abstract Methods   
   @abstractmethod
   def root(self):
     
     ''' Returns the address of the root node'''

     pass
   
   @abstractmethod
   def parent(self,pos):
     
     ''' Returns the address of the parent of a given node , node 
     address (pos)
     '''

     pass
   
   @abstractmethod

   def children(self,pos):
     
     ''' Returns the address of the children of a given node, at 
     an address 'pos'''
   
     pass
   
   def num_children(self,pos):
     
     ''' Returns the number of children of a given node(node address-pos)'''

     pass
   
   def __len__(self):
     
     '''Returns the length of the tree'''

     pass
   

   #Concete Methods

   def isroot(self,pos):
     
     '''Returns True if the given address,pos is the root of the Tree'''
     return self.root()==pos
   
   def isleaf(self,pos):
     
     ''' Returns True if the given node is a leaf node (number of child nodes=0)'''

     return self.num_children(pos)==0
   
   def isempty(self):
     
     ''' Returns True if the length of the tree is 0 , no elements within the tree'''

     return len(self)==0
   
   def depthN(self,pos):
     
     ''' Returns the depth of a given node position(pos)'''
     
     if self.isroot(pos)==True:
       return 0
     return 1 + self.depthN(self.parent(pos))
   
   def heightN(self,pos):
     
     ''' Returns the height - the child node with the maximum length +1 value 
     for a given node in a tree'''
     
     if self.isleaf(pos)==True:     # Check for root
       
       return 0
     
     else:
       count=0
       for child_node in self.children(pos):
         x=self.heightN(child_node)
         if x>count:
           count=x
       return count
     
   def height(self):
     
     ''' Returns the heigth of the tree - height of the root node'''
     
     if self.isempty()==False:
       
       pos=self.root()
       return self.heightN(self,pos)

####

class AbstractBinaryTree(AbstractTree):

    ''' Abstract Methods:
                            left()
                            right())
                            
        Concrete Methods:
                            children()
                            sibling()'''

    @abstractmethod

    def left(self,pos):

        ''' Returns the address of the left child of a given node'''

        pass

    @abstractmethod

    def right(self,pos):

        ''' Returns the address of the right child of a given node'''

        pass

    def children(self,pos):

        ''' Returns the children of a given node address'''

        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)
        else:
            return None
        
    def sibling(self,pos):

        '''Returns the sibling of a given node - right child if the given node is a left child
        and vice-versa'''

        parent=self.parent(pos)

        if parent is None:

            return None

        else:

            if self.left(parent)==pos:

                yield self.right(parent)

            else:

                yield self.left(parent)
    

####


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
    
    def __init__(self,item=None,left=None,right=None,parent=None):

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

T=LinkedBT(1)
print(T)
T.addLeft(2,T.root)
T.addRight(3,T.root)
T.addLeft(4,T.root.left)
T.addRight(5,T.root.left)
T.addLeft(6,T.root.right)
T.addRight(7,T.root.right)
print(T)


     


   
