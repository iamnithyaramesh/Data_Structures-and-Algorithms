def partition(arr,low,high):

    pivot = arr[high]

    i = low-1 #remembers the before position where the index is stored

    for j in range(low,high):

        if arr[j]<=pivot:
            


            #swap with the place of the start index

            i+=1

            (arr[i],arr[j]) = (arr[j],arr[i])
            

    
    #swap the position of the pivot

    arr[high],arr[i+1] = arr[i+1],arr[high]
    return i+1


def quick_sort(arr,low,high):

    if low<high:
        p = partition(arr,low,high)
    

        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
    

print('-------')
arr = [10,7,9,4,63]
quick_sort(arr,0,4)
print(arr)