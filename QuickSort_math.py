def partition(arr,begin,end):
    pivot = arr[end]
    i = (begin-1)

    for j in range(begin,end):
        if(arr[j] <= pivot):
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[end] = arr[end],arr[i+1]
    return(i+1)

def quicksort(arr, begin, end):
    if len(arr) == 1:
        return arr
    if begin < end:
        p = partition(arr, begin, end)
        quicksort(arr, begin, p-1)
        quicksort(arr, p+1, end)


x =[]
total = 0
while True:
        line = input("Enter an integer: ")
        if line:
            try:
                number = int(line)
            except Exception as e:
                print(str(e))
                continue
            x.append(number)
        else:
            break

n =len(x)

# Quicksort does not need to be implemented, you can just use x.sort() for a permanent sort or sorted(x) for a temp sort
quicksort(x,0,n-1)

if(n % 2 == 0):
    median = int(n/2)
else:
    median = int((n-1)/2)

# min(), max(), and sum() functions do not require a sorted list. Nor the bullshit of saving variables on a simple list.
if n:
    print("Count =", n, "\nTotal =", sum(x), "\nMean =", total/n, "\nMin =", min(x), "\nMax =", max(x), "\nMedian =", x[median])
    print(x)
