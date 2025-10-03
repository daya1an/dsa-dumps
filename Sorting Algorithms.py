#Bubble Sort

def bubble_sort(arr):

    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr




if __name__ == '__main__':

    # elements = [ 5, 81, 64, 1, 2, 39, 40, 10]
    elements = [1, 2, 5, 10, 39, 40, 64, 81]
    names = ["daya","devi","michael","andrew","jeni","rajan","joy","kiran"]
    # print(bubble_sort(names))

