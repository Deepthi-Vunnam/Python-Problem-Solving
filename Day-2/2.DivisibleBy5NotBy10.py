# 2. Divisible by 5 but Not by 10
# Question: Check if a number is divisible by 5 but not by 10.
# Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0.
# - Input: Number = 25 - Output: Satisfy

n = int(input("Enter Number:"))
if (n % 5 == 0) and (n % 10 != 0):
    print("Satisfy")
else:
    print("Not satisfy")