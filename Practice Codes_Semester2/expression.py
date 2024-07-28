from linkedbt import LinkedBT

class Expression(LinkedBT):

    def __init__(self,item=None,left=None,right=None):

        super().__init__(item,left,right)
    
    def construct(self,input_str):

        s=[]
        for ch in input_str:
            if ch not in '+-/*':
                s.append(LinkedBT.LinkedNode(ch))
            else:
                r_child=s.pop()
                l_child=s.pop()
                s.append(LinkedBT.LinkedNode(ch,l_child,r_child))
        return s.pop()

E=Expression()
E.construct('ab+c-')
print(E)