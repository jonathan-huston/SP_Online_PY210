#!/usr/bin/env python3

def fibonacci(n):
    """Returns the nth element of the fibonacci sequence.  Note that n is 0-based."""
    return sum_series(n)

def lucas(n):
    """Returns the nth element (0-based) of the lucas numbers."""
    return sum_series(n, 2, 1)

def sum_series(n, a = 0, b = 1):
    """Returns the nth element (note: n is 0-based) of the fibonacci series.

    Specifying a and b will override the default start points of the series.
    """
    if n == 0: return a
    elif n == 1: return b
    else:
        for i in range(2,n+1):
            sum = a + b
            a = b
            b = sum
        return sum

if __name__ == "__main__":
    assert fibonacci(7) == sum_series(7, 0, 1) # Since fibonacci() is just calling back to sum_series, let's ensure we implemented the logic correctly
    assert lucas(12) == sum_series(12, 2, 1) # Same here for lucas()

    assert lucas(7) == 29 # The 7th element is 29 -- validate that here
    assert fibonacci(7) == 13 # The 7th element should be 13
