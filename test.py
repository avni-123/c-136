multiples=[3,7,6,14,7,21,12,28,15,35]
'''
1. take even numbers
2. take the half value
'''

# for i in multiples:
#     if i%2 ==0:
#         even_numbers = i/2
#         print(even_numbers)

'''
LIST COMPREHENSION
[expression loop-statment condition]
'''

even_numbers = [i/2 for i in multiples if i%2 ==0]
print(even_numbers)

