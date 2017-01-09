def is_prime(num):
    prime = True
    if num == 0 or num == 1:
        prime = False
    elif num >= 2:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                prime = False
                break
    else:
        prime = False
    return prime

print(is_prime(100000000))
