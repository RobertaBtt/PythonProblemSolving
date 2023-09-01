__author__ = 'RobertaBtt'


# O(N + M)
# https://app.codility.com/demo/results/trainingB5JAHK-966/ 88%
# https://app.codility.com/demo/results/training4T899S-UKK/ 100%

def solution(N, A):
    to_the_max = 0
    counter = [to_the_max] * N
    last_max = False
    for value in A:
        if value == N + 1 and not last_max:
            counter = [to_the_max] * N
            last_max = True
            continue
        if value <= N:
            counter[value - 1] += 1
            to_the_max = max(counter[value - 1], to_the_max)
            last_max = False

    return counter


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
