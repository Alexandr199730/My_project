import os
os.system("cls")

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(5))  # Выведет 120
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(7))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Устанавливаем границы поиска
    
    while left <= right:
        mid = (left + right) // 2  # Находим середину списка
        
        if arr[mid] == target:
            return mid  # Элемент найден, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент справа, сдвигаем границу
        else:
            right = mid - 1  # Искомый элемент слева, сдвигаем границу

    return -1  # Элемент не найден

numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# numbers = sorted(numbers)
target = 23

result = binary_search(numbers, target)
print("Элемент найден на индексе:", result) 
print("Демонстрация поиска")
print("Удалённый репозиторий подключён")
# n = 1234//10
# print(n)
