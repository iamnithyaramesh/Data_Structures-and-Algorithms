from LinkedBinaryTree import LinkedBinaryTree

class Expression(LinkedBinaryTree):

    def __init__(self,item=None,t_left=None,t_right=None):

        super().__init__(item,t_left,t_right)

    def construct(self,input_string):
        s=[]
        for i in input_string:
            if i not in '+-/*':
                s.append(Expression(i))
            else:
                r_child=s.pop()
                l_child=s.pop()
                s.append(Expression(i,l_child,r_child))
        self.root=s.pop().getRoot()
        return self.root

E=Expression()
E.construct('ab+c-')
print(E)