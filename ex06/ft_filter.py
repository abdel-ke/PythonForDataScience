def ft_filter(function, items):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None,
    return the items that are true."""
    if function is None:
        def function(x):
            return x
    return [x for x in items if function(x)]
