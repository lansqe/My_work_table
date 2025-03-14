def delete_nth(order, max_e):
    new_lst = []
    for num in order:
        if new_lst.count(max_e) < max_e:
            new_lst.append(num)
    return new_lst


print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 2))
