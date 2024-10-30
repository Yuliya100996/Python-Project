def is_prime(func):
    def wrapper(a, b, c):
        d = func(a, b, c)
        count = 0
        for i in range(2, d + 1):
            if d % i == 0:
                count += 1
                print('составное')
            else:
                print('простое')
            return d
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)