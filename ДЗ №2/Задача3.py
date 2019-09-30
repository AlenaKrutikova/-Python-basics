def quicksort(lst):
    if len(lst) <= 1: return lst
    else:
        median = lst[len(lst)//2]
        less = []
        more = []
        average = []
        for el in lst:
            if el < median : less.append(el)
            elif el > median : more.append(el)
            else: average.append(el)
    return quicksort(less) + average + quicksort(more)