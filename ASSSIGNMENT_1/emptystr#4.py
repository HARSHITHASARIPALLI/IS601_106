#hs759
#Name: Harshitha Saripalli
#Date of Submission:02/17/2024

# Question 4
arr1 = ['apple', '', 'banana', '', 'cherry'] #1
arr2 = ['', 'dog', '', 'cat', ''] #2
arr3 = ['hello', '', 'world', '', ''] #3
arr4 = ['', '', '', '', ''] #4
arr5 = ['one', '', 'two', '', 'three'] #5
# Remove empty strings from the above lists and output the lists (print the output for all lists)
def empty_str(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
    #your code here
    N=[]
    for i in arr:
        if i!='':
            N.append(i)
    print(N)
    print('\n End of empty str values')
empty_str(1, arr1)
empty_str(2, arr2)
empty_str(3, arr3)
empty_str(4, arr4)
empty_str(5, arr5)
