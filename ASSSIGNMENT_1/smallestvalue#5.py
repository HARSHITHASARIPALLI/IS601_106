#hs759
#Name: Harshitha Saripalli
#Date of Submission: 02/17/2024 
# Question 5
# Write a function that takes in a list and prints the smallest value from that list.
A = [15,26,2,14]
if len(A) == 0:  # Check if the list is empty by comparing its length to 0
    print("The list is empty.")
else:
    s = A[0]  # Initialize the smallest value with the first element
    for i in A:
        if i < s:
            s = i
    print("The smallest value in the list is:", s)  
    print('\n End of converted sum values') 