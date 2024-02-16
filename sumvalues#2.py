# Question 2
arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # 1
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20] #2
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44] #3
# Only output the sum/total of the lists values (print the output for all lists)
def sum_values(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
    #your code here
    sum=0
    for i in arr :
        sum=sum+i
    print(sum)
    print('\n End of sum values')
sum_values(1,arr1)
sum_values(2,arr2)
sum_values(3,arr3)
