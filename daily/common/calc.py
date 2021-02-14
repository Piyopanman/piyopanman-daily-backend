def calc_eva(list):
    sum = 0
    for eva in list:
        sum += list[eva]

    for eva in list:
        list[eva] = list[eva] / sum * 100

    return list
