#Bubble Sort

def simple_bubble_sort(arr):

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

def complex_bubble_sort(elements, key):
    for i in range(len(elements)-1):
        swapped = False
        for j in range(len(elements)-1-i):
            if elements[j][key] > elements[j+1][key]:
                elements[j][key],elements[j + 1][key] = elements[j + 1][key],elements[j][key]
                swapped = True

        if not swapped:
            return elements

    return elements


if __name__ == '__main__':

    # elements = [ 5, 81, 64, 1, 2, 39, 40, 10]
    # elements = [1, 2, 5, 10, 39, 40, 64, 81]
    names = ["daya","devi","michael","andrew","jeni","rajan","joy","kiran"]
    print(simple_bubble_sort(names))

    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    print(complex_bubble_sort(elements,key='transaction_amount'))

    #output:
    # [{'name': 'mona', 'transaction_amount': 200, 'device': 'iphone-10'},
    #  {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    #  {'name': 'kathy', 'transaction_amount': 800, 'device': 'vivo'},
    #  {'name': 'aamir', 'transaction_amount': 1000, 'device': 'iphone-8'}]

    print(complex_bubble_sort(elements, key='name'))

    # output:
    # [{'name': 'aamir', 'transaction_amount': 200, 'device': 'iphone-10'},
    #  {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    #  {'name': 'kathy', 'transaction_amount': 800, 'device': 'vivo'},
    #  {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-8'}]


