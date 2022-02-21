from hwfunctions import fun_factor, fun_inc


def delayed_increment(c, start, end):
    x = dask.delayed(inc)(c)
    y = dask.delayed(inc)(start)
    z = dask.delayed(inc)(end)
    total = dask.delayed(sum)(fun_inc)  
    pass


def delayed_factor(c, start, end):
    x = dask.delayed(inc)(c)
    y = dask.delayed(inc)(start)
    z = dask.delayed(add)(end)
    total = dask.delayed(sum)(fun_factor)
    pass


def future_increment(c, start, end):
    # use fun_inc
    pass


def future_factor(c, start, end):
    # use fun_factor
    pass
