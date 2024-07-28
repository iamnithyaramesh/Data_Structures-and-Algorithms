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
     mid=len(seq)//2
     return(merge(merge_sort(seq[:mid]),merge_sort(seq[mid:])))
    

def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
    
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr

print(merge_sort([4,5,2,7,1,8]))
print(quicksort([4,5,2,7,1,8],0,5))
