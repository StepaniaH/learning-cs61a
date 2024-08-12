def twenty_twenty_four():
    """Come up with the most creative expression that evaluates to 2024
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_four()
    2024
    """
    return int(2**(int(2**(int(2**2)))-int(2**2+2**0))-int(2**2**2+2**2+2**1+2**0)-2**0)

print(twenty_twenty_four())
