def ft_filter(function, items):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        def function(x):
            """ define a function that returns x"""
            return x
    return [x for x in items if function(x)]
