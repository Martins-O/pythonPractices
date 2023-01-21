def is_prime(number):
    if number in [2, 3]:
        return True
    if (number == 1) or (number % 2 == 0):
        return False
    r = 3
    while r * r <= number:
        if number % r == 0:
            return False
        r += 2
    return True
