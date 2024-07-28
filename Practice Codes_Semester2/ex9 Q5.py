from ex9 import Stack

''' '''

class In_Post_Conversion:

    def __init__(self,exp):
        self.exp=exp
        self.operand_stack=Stack()
        self.operator_stack=Stack()
    
    def push_stack(self):
        for i in self.exp:
            print(i)
            if i.isalnum()==True:
                self.operand_stack.push(i)
            elif not(i.isalnum()) and i!="'":
                self.operator_stack.push(i)
    



Exp1=In_Post_Conversion('2+5*9')


    
            



    
