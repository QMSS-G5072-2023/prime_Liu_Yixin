import math

def is_prime(n):

    """
    The function is to check the giving number if is prime.

    Parameters:
    ----------
    n : int
        The number to check if it is prime.

    Returns:
    -------
    bool
        True means the number is prime number. False otherwise.

    Example:
    -------
    >>> is_prime(2)
    True

    >>> is_prime(4)
    False
    """
        
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
