# import sys
#
# n = int(sys.stdin.readline())
#
#
# def bracket(count, s='', left=0, right=0):
#     if left == count and right == count:
#         print(s)
#     else:
#         if left < count:
#             bracket(count, s + '(', left + 1, right)
#         if right < left:
#             bracket(count, s + ')', left, right + 1)
#
#
# bracket(n, s='', left=0, right=0)



import numpy as np

k = 6  # количество скобок
init = list(np.zeros(k))  # пустой список, куда кладем скобки
cnt = 0  # разница между скобками
ind = 0  # индекс, по которому кладем скобку в список


def f(cnt, ind, k, init):
    # кладем откр. скобку, только если хватает места
    if (cnt <= k - ind - 2):
        init[ind] = '('
        f(cnt + 1, ind + 1, k, init)
    # закр. скобку можно положить всегда, если cnt > 0
    if cnt > 0:
        init[ind] = ')'
        f(cnt - 1, ind + 1, k, init)
    # выходим из цикла и печатаем
    if ind == k:
        if cnt == 0:
            print(init)


f(cnt, ind, k, init)
