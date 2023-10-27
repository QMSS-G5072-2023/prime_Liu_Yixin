import pytest

from prime_yl5418.prime_yl5418 import is_prime


def test_is_prime():
    assert is_prime(2), 'Error: your input is a prime number'
    assert is_prime(7), 'Error: your input is a prime number'
    
    # Test using a composite numbers (e.g. 8, 9)
    assert not is_prime(8), 'Error: your input is not a prime number'
    assert not is_prime(9), 'Error: your input is not a prime number'
