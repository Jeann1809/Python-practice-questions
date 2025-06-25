# Problem 1: Happy number

# Understand: 12 = 1*1 + 2*2
def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# Ejemplos
print(isHappy(19))   # True (porque sí es un número feliz)
