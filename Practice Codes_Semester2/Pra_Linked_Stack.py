'''class LNode:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class Linked_Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isempty(self):
        return self.size == 0

    def push(self, item):
        temp = LNode(item)
        temp.next = self.top
        self.top = temp
        self.size += 1

    def pop(self):
        if self.isempty():
            return "Stack is Empty"
        del_item = self.top.item
        self.top = self.top.next
        self.size -= 1
        return del_item

    def peek(self):
        if self.isempty():
            return "Stack is Empty"
        return self.top.item

    def display(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            s = "["
            current = self.top
            while current is not None:
                s += str(current.item) + "-->"
                current = current.next
            s += "]"
            print(s)

S1 = Linked_Stack()
print(S1.isempty())
S1.push(10)
S1.display()
S1.push(20)
S1.display()
S1.push(30)
S1.display()
print(S1.pop())
print(S1.peek())
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str=''
        list=s.lower().split(',')
        for i in list:
            if i not in':':
             new_str+=i
        return new_str
    
C=Solution()
   
print(C.isPalindrome("A man, a plan, a canal: Panama"))

    
                
