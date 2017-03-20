def replicate_iter(times,data):
    Array = []
    if type(times) != int or not isinstance(data, (int, float, complex, str)):
        raise ValueError ('Invalid Value')
    elif times < 0:
        return []
    else:
        for x in range (times):
            Array.append(data)
        return Array


def replicate_recur(times,data):
    Array = []
    if type(times) != int or not isinstance(data, (int, float, complex, str)):
        raise ValueError ('Invalid Value')
    elif times <= 0:
        return []
    else:
       Array = replicate_recur(times-1,data)
       Array.append(data)
    return Array
