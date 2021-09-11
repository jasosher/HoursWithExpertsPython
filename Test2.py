import sys


def Get_Next_Largest_numbers(n):
    numbers = list(str(n))
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] < numbers[i + 1]:
            a = numbers[i:]
            b = min(filter(lambda x: x > a[0], a))
            a.remove(b)
            a.sort()
            numbers[i:] = [b] + a
            return int("".join(numbers))
    return -1


n = 12
print("Input:", n)
print("Output:", Get_Next_Largest_numbers(n))

n = 21
print("\nInput:", n)
print("Output:", Get_Next_Largest_numbers(n))

n = 12345678
print("\nInput:", n)
print("Output:", Get_Next_Largest_numbers(n))

n = 34535762
print("\nInput:", n)
print("Output:", Get_Next_Largest_numbers(n))

n = 45590051
print("\nInput:", n)
print("Output:", Get_Next_Largest_numbers(n))

n = 987654321
print("\nInput:", n)
print("Output:", Get_Next_Largest_numbers(n))