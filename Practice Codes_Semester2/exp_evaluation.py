from LinkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):

    def __init__(self,item=None,left=None,right=None):

        super().__init__(item,left,right)
    
    def construct(self,input_expression):
        s=[]
        for ch in input_expression:
            if ch not in '()+-*/':
                s.append(ExpressionTree(ch))
            else:
                r_child=s.pop()
                l_child=s.pop()
                s.append(ExpressionTree(ch,l_child,r_child))
            
        self.root=s.pop().getRoot()
        return self.root

    def evaluate(self,input_expression):
        s=[]
        value=0
        for ch in input_expression:
            if ch not in '()+-*/':
                s.append(ExpressionTree(ch))
            else:
                r_node=s.pop()
                l_node=s.pop()
                r_child=int(r_node.item)
                l_child=int(l_node.item)
                if ch=="+":
                    value+=(r_child+l_child)
                elif ch=="-":
                    value+=(r_child-l_child)
                elif ch=="*":
                    value+=(r_child*l_child)
                elif ch=="/":
                    value+=(r_child/l_child)
                s.append(ExpressionTree(ch,l_node,r_node))
            print(value)

E=ExpressionTree()

E.evaluate('12+3-')



