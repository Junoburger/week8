def avg_val(lst):
    elems_sum = 0
    for elem in lst:
        elems_sum += elem
    average = elems_sum / len(lst)
    return int(average)
