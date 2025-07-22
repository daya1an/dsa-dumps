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
