#! /usr/bin/env python3


def linear_search(A, n, x):
    """Linear search (pg. 13). Worst case: Θ(n). Best case: Θ(1). Does not
        require sorted array.
    
    Args:
        A (list): an array.
        n (int): the number of elements in A to search through.
        x: the value being searched for.

    Returns:
        Index i (int) for which A[i] = x. -1 (int) if x not found in A.

    """
    answer = -1
    for i in range(n):
        if A[i] == x:
            answer = i
    return answer


def better_linear_search(A, n, x):
    """Better linear search (pg. 14). Same Args, Returns, and complexity as 
        above. 

    Args:
        A (list): an array.
        n (int): the number of elements in A to search through.
        x: the value being searched for.

    Returns:
        Index i (int) for which A[i] = x. -1 (int) if x not found in A.

    """
    for i in range(n):
        if A[i] == x:
            return i
    return -1


def sentinel_linear_search(A, n, x):
    """Sentinel linear search (pg. 16). Same Args, Returns, and complexity as
        above.

    Args:
        A (list): an array.
        n (int): the number of elements in A to search through.
        x: the value being searched for.

    Returns:
        Index i (int) for which A[i] = x. -1 (int) if x not found in A.

    """
    m = n - 1   # since python uses 0-indexing
    last = A[m]
    A[m] = x
    i = 1
    while A[i] != x:
        i += 1

    A[m] = last
    if (i < m) or (A[m] == x):
        return i
    else:
        return -1
   

def factorial(n):
    """Factorial function (pg. 23).

    Args:
        n (int): non-negative integer.
        
    Returns:
        int: n!

    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def bad_factorial(n):
    """Bad factorial function (pg. 24). 

    Args:
        n (int): non-negative integer.

    Returns:
        int: n! (but should actually give "RecursionError: maximum recursion 
            depth exceeded in comparison", a stack overflow error).

    """
    if n == 0:
        return 1
    else:
        return (bad_factorial(n+1)) / (n + 1)


def recursive_linear_search(A, n, i, x):
    """Recursive linear search (pg. 24). Searches for a value in every element
        of an array after a certain index. Same Args (with an added parameter 
        i) and complexity as "linear_search".

    Args:
        A (list): an array.
        n (int): the number of elements in A to search through.
        i (int): the index of the first element of A to begin searching.
        x: the value being searched for.

    Returns:
        Index i (int) for which A[i] = x in the subarray A[i..n]. -1 (int) if 
            x not found in A[i..n].

    """
    if i > n:
        return -1
    elif (i <= n) and (A[i] == x):
        return i
    elif (i <= n) and (A[i] != x):
        return recursive_linear_search(A, n, i+1, x)
       
    
