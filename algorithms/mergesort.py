def mergesort(A, left=None, right=None):
    '''
    Mergesort algorithm

    Objectives:
        O(nlogn) runtime
        O(n) space utilization (~2n)


    >>> mergesort([4,2,3,1])
    [1, 2, 3, 4]
    >>> mergesort([])
    []
    >>> mergesort([9,4,2,7,9,4,2])
    [2, 2, 4, 4, 7, 9, 9]
    '''
    left = left or 0
    right = right or len(A)
    if (right - left) > 1:
        center = left + ((right - left) / 2)
        mergesort(A, left, center)
        mergesort(A, center, right)
        merge(A, left, center, right)
    return A

def merge(A, left, center, right):
    L = A[left:center]
    R = A[center:right]
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[left] = L[i]
            i += 1
        else:
            A[left] = R[j]
            j += 1
        left += 1

    while i < len(L):
        A[left] = L[i]
        i += 1
        left += 1

    while j < len(R):
        A[left] = R[j]
        j += 1
        left += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()