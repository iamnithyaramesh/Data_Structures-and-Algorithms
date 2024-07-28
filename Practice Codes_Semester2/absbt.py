from abstree import AbstractTree

from abc import abstractmethod

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
    

