class Single_Node:

    __slots__=['item','next']

    def __init__(self,item=None,next=None):

        self.item=item
        self.next=next

class Double_Node:

    __slots__=['item','next','prev']

    def __init__(self,item=None,next=None,prev=None):

        self.item=item
        self.next=next
        self.prev=prev
    









