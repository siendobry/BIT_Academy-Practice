def next_prime(y):
    y += 1

    def is_prime(x):
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    while not is_prime(y):
        y += 1
    return y

print(next_prime(5))