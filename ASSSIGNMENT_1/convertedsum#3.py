#hs759
#Harshitha Saripalli
#Date of Submission:02/17/2024

# Question 3
arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100] #1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233] #2 
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33] #3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99] #4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30] #5
# Convert the negative values in the following lists to positive and ouput the sum of all values (print the output for all lists).
def converted_sum_values(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
    #your code here
    sum=0
    for k in arr:
              if k<0:
                      k=k*-1
              sum=sum+k  
    print(sum)
    print('\n End of converted sum values')
converted_sum_values(1,arr1)
converted_sum_values(2,arr2)
converted_sum_values(3,arr3)
converted_sum_values(4,arr4)
converted_sum_values(5,arr5)
