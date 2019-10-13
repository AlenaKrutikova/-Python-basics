l = []
lst = [1, 2, 3, [1, 2, [5, [6]]], 7]

def flat_list_recurs(lst):
    for e in lst:
        if type(e) != list:
            l.append(e)            
        else:
            flat_list_recurs(e)
    return l

print(flat_list_recurs(lst))
        
