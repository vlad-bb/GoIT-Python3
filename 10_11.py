
def factorial(n):
    if n < 2:
        return 1  # Базовый случай
    else:
        return n * factorial(n - 1)  # Рекурсивный случай
        
def factorial(k):
    if k < 2:
        return 1  # Базовый случай
    else:
        return k * factorial(k - 1)  # Рекурсивный случай
        
def number_of_groups(n, k):
    result = int(factorial(n) / (factorial(n) - factorial(k)) * factorial(k))
    return result
