def ft_filter(function, item):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None,
    return the items that are true."""
    lst = list()
    for i in item:
        if function(i):
            lst.append(i)
    return lst
