def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    r = []
    for num in range(x, (n+1)*x, x):
        r.append(num)
    return r