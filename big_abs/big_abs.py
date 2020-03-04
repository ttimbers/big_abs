def largest_absolute_value(a, b):
    """
    Return the largest absolute value, a or b

    Parameters
    ----------
    a : int or float
        A number that you want to know if its absolute value is larger than that of b
    b : int or float
        A number that you want to know if its absolute value is larger than that of b

    Returns
    -------
    int or float
        The number which has the largest absolute value (either a or b)

    Examples
    --------
    >>> largest_absolute_value(-25, 20)
    -25
    """
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a >= b:
        return a
    else:
        return b
