from abc import ABC
from abc import abstractmethod


class AbstractTree(ABC):

    class AbsNode:
        def __init__(self,item=None,parent=None):

            self.item=item
            self.parent=parent
            self.child=[]
            self.size=0

    def getRoot(self):

        return self.isRoot

    def getParent(self, pos):
        
        if pos.parent is None:
            return ValueError
        return pos.parent

    def getNum_children(self, pos):
        
        if pos.child is None:
            return ValueError
        return len(pos.child)

    def getChildren(self, pos):
        
        if pos.child is not None:
            return pos.child

    def __len__(self):

        return self.size

    def isRoot(self, pos):
        """Returns True if the given position 'pos' is the root of the tree, False otherwise."""
        return self.getRoot() == pos

    def isLeaf(self, pos):
        """Returns True if the given position 'pos' is a leaf node (has no children), False otherwise."""
        return self.getNum_children(pos) == 0

    def isEmpty(self):
        """Returns True if the tree is empty (has no positions), False otherwise."""
        return len(self) == 0

    def depthN(self, pos):
        """
        Returns the depth of the position 'pos' in the tree.
        Depth is the number of edges in the path from the root to 'pos'.
        """
        if self.isRoot(pos):
            return 0
        return 1 + self.depthN(self.getParent(pos))

    def heightN(self, pos):
        """
        Returns the height of the position 'pos' in the tree.
        Height is the number of edges in the longest path from 'pos' to a leaf.
        """
        if self.isLeaf(pos):
            return 0
        return 1 + max([self.heightN(child) for child in self.getChildren(pos)])

    def height(self):
        """Returns the height of the tree (i.e., the height of the root position)."""
        return self.heightN(self.getRoot())

A=AbstractTree()
A.insert(2)