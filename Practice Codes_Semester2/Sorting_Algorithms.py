c
def bubble_sort(seq):
    n=len(seq)
    for i in range(n-1):
        for j in range(n-i-1):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1]=seq[j+1],seq[j]
    return seq

def selection_sort(seq):
    n=len(seq)
    for i in range(n):
        for j in range(i+1,n):
            if seq[i]>seq[j]:
                seq[i],seq[j]=seq[j],seq[i]
    return seq

def insertion_sort(seq):
    n=len(seq)
    for i in range(n):
        temp=seq[i]
        j=i-1
        while j>=0 and seq[j]>=temp:
            seq[j+1]=seq[j]
            j=j-1
            seq[j+1]=temp
    return seq

def merge(l1,l2):
    l3=[]
    i=0
    j=0
    try:
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

def merge_sort(seq):
    if len(seq)==1:
        return seq
    else:
        n=len(seq)//2
        return merge(merge_sort(seq[:n]),merge_sort(seq[n:]))

def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
    return arr

print(bubble_sort([4,5,2,7,1,8]))
print(selection_sort([4,5,2,7,1,8]))
print(insertion_sort([4,5,2,7,1,8]))
print(merge_sort([4,5,2,7,1,8]))
print(quick_sort([4,5,2,7,1,8],0,5))
