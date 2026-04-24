def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    less = []
    equal = []
    greater = []

    for x in array:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quick_sort(less) + equal + quick_sort(greater)