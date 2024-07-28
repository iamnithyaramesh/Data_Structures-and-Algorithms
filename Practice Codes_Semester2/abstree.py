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
     


   
