from ex9 import Queue

class PQueue:

   def __init__(self):
      self.hpq=Queue()
      self.lpq=Queue()

   def enqueue(self,priority,ele):
      if priority==0:
         self.hpq.enqueue(ele)
      elif priority==1:
         self.lpq.enqueue(ele)
   
   def dequeue(self):
      if not(self.hpq.__isempty__()):
         self.hpq.dequeue()
      else:
         self.lpq.dequeue()
   
   def __str__(self):
      return "High Priority"+str(self.hpq)+'\n'+"Low Priority"+str(self.lpq)
      
PQ=PQueue()
PQ.enqueue(0,10)
print(PQ)
PQ.enqueue(0,20)
print(PQ)
PQ.enqueue(0,30)
print(PQ)
PQ.enqueue(1,10)
print(PQ)
PQ.enqueue(1,20)
print(PQ)
PQ.enqueue(1,30)
print(PQ)
PQ.dequeue()
print(PQ)
PQ.dequeue()
print(PQ)
PQ.dequeue()
print(PQ)
PQ.dequeue()     
print(PQ) 
    
    
