# 1. Check Even or Odd
# Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. 
# Otherwise, it’s odd.- Input: Number = 6 - Output: Even number

n = int(input("Enter Value:"))
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")