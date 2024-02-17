# UCID:hs759
# Name: Harshitha Saripalli
# Date of submission :02/17/2024
arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 1
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 2
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9] # 3

# only output the odd values from the above lists (print the output for all lists)
def odd_values(num,arr): # pass the num as list number and arr as list name
    print('output for arr {num} of odd values: \n')
    odd_list = [x for x in arr if x % 2 != 0]
    print(odd_list)


odd_values(1, arr1)
odd_values(2, arr2)
odd_values(3, arr3)
print('\n End of odd values')