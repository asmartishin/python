def row_sum_odd_numbers(n):
    array = [x for x in range((1 + n) * n) if x % 2 == 1]
    return(sum(array[n * (n - 1) / 2:]))

print(row_sum_odd_numbers(13))