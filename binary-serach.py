def binSrch(arr,t):
    n = len(arr)
    s = 1
    e = n-1
    ans = [False, -1] 
    while s <= e:
        
        m = (s+e)//2
        print(m)
        if (arr[m] == t):
            ans[0] = True
            ans[1] = m+1
        
        if (arr[m]>t):
            e = m-1
        else:
            s = m+1
    
    return ans

arr = [3, 6, 8, 9, 21, 52, 63, 79, 85, 100, 150]
print("Answer : ",binSrch(arr,79))

#better version
def binarySearch(arr, e):
    start = 0
    end = len(arr) - 1
    mid = len(arr) // 2

    while start < end:
        mid = (start + end) // 2

        # print(arr[start], arr[mid], arr[end])

        if arr[mid] == e:
            return mid
        elif arr[start] == e:
            return start
        elif arr[end] == e:
            return end

        if e > arr[mid]:
            start = mid+1
        else:
            end = mid-1

    return mid


print(binarySearch([3, 25, 37, 41, 56, 72, 91, 100], 25))
