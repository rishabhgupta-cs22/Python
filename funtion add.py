# def sumsquare(l):
#     odd_sum = 0
#     even_sum = 0

#     for num in l:
#         if num % 2 == 0:  # Even number
#             even_sum += num ** 2
#         else:  # Odd number
#             odd_sum += num ** 2

#     return [odd_sum, even_sum]
def find_largest_number(num1, num2, num3):
    largest = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 else num3
    return largest