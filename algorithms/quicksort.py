def quicksort(A, left=None, right=None):
    '''
    Quicksort algorithm

    Objectives:
        O(nlogn) runtime
        O(n) space utilization (~2n)


    >>> quicksort([4,2,3,1])
    [1, 2, 3, 4]
    >>> quicksort([9,4,2,7,9,4,2])
    [2, 2, 4, 4, 7, 9, 9]
    >>> quicksort([])
    []
    '''
    left = left or 0
    right = right or len(A)
    if (right - left) > 1:
        i = partition(A, left, right)
        quicksort(A, left, i)
        quicksort(A, i+1, right)
    return A

def partition(A, left, right):
    pivot = A[right-1]
    i = left
    for j in xrange(left, right-1):
        if A[j] <= pivot:
            swap(A, i, j)
            i += 1
    swap(A, i, right-1) # put pivot in position i
    return i

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


if __name__ == "__main__":
    import doctest
    doctest.testmod()