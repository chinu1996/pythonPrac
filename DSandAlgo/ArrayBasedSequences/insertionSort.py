# Insertion sort algorithm with o(n^2) complexity
def insertionSort(A):
    """Sort the comparable element in non decreasing order"""
    for k in range(1, len(A)):   #from 1 to n-1
        cur= A[k]               #current element to be inserted
        j=k
        while j>0 and j-1> cur:
            A[j] = A[j-1]
            j = j-1
        A[j]=cur           #cur is now at its correct position