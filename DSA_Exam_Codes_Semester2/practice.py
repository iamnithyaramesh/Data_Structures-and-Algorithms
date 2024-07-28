'''def binary_search(seq,item,low,high):

    seq.sort()
    if low>high:
        return False
    else:
        mid=low+high//2
        if item==seq[mid]:
            return True
        elif item<seq[mid]:
            return binary_search(seq,item,low,mid-1)
        elif item>seq[mid]:
            return binary_search(seq,item,mid+1,high)

print(binary_search([6,3,4,2,1],4,0,5))'''

def bubble_sort(seq):
    n=len(seq)
    for i in range(n-1):
        for j in range(n-i-1):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1]=seq[j+1],seq[j]
    return seq

print(bubble_sort([5,4,3,2,1]))

def selection_sort(seq):
    n=len(seq)
    for i in range(n-1):
        for j in range(i,n):
            if seq[i]>seq[j]:
                seq[i],seq[j]=seq[j],seq[i]
    return seq

print(selection_sort([5,4,3,2,1]))

def insertion_sort(seq):
    n=len(seq)
    for i in range(n):
        temp=seq[i]
        j=i-1
        while j>=0 and seq[j]>temp:
            seq[j+1]=seq[j]
            j=j-1
        seq[j+1]=temp
    return seq

print(insertion_sort([5,4,3,2,1]))

def merge(l1,l2):
    l3=[]
    try:
     while True:
        i=0
        j=0
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

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    n = len(seq) // 2
    left_half = merge_sort(seq[:n])
    right_half = merge_sort(seq[n:])
    return merge(left_half, right_half)
print(merge_sort([5,4,3,2,1]))
            
