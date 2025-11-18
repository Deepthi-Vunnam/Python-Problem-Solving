# 4. Smallest Among Two Numbers
# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value.
# - Input: A = 4, B = 7 - Output: Smallest is: 4

A = int(input("Enter A:"))
B = int(input("Enter B:"))
if A<B:
    print("smallest value is:",A)
else:
    print("smallest value is :",B)