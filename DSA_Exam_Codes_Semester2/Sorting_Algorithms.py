#Merge_Sort

def merge(l1,l2):
    l3=[]
    i=0
    j=0
    try:
        if not(isinstance(l1,list)) or not(isinstance(l2,list)):
         raise IndexError("Not a List")
        else:
         while True:
            if l1[i]<l2[j]:
                l3.append(l1[i])
                i+=1
            else:
                l3.append(l2[j])
                j+=1
    except IndexError:
        if i==len(l1):
            l3.extend(l2[j:])
        else:
            l3.extend(l1[i:])
    return l3

def merge_sort(l):
    n=len(l)//2
    if len(l)<=1:
        return l
    else:
        return merge(merge_sort(l[:n]),merge_sort(l[n:]))

print(merge_sort((1,2,3,4,5)))
print(merge_sort([5,4,3,2,1]))
print(merge_sort([4,2,5,1,3]))

#Merge Sort using Linked Queues

#Quick_Sort

#Pivot as the end element

'''def partition(l,begin,end):
    pivot=l[end]
    i=0
    j=end-1
    while i<=j:
        while (l[i]<pivot):
            i=i+1
        while (l[j]>pivot):
            j=j-1
        if i<=j:
            l[i],l[j]=l[j],l[i]
            i+=1
            j+=1
    if i<end:
        l[end],l[i]=l[i],l[end]
    return i

def quick_sort(l,begin,end):
    if begin<end:
        k=partition(l,begin,end)
        l1=quick_sort(l,begin,k-1)
        l2=quick_sort(l,k-1,end)
        return l1.extend(l2)

l=[1,2,3,4,5]
print(quick_sort(l,0,len(l)-1))'''





    