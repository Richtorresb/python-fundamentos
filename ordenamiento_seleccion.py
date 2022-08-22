list = [8,5,2,6,9,3,1,4,0,7]

def selector(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

        

selector(list)
print(list)