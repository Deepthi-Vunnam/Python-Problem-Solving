# 7. Break Amount into 1000s, 500s, and Remaining Change
# Question: Break the total amount into denominations.
# - Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200

Amount = int(input("Enter Amount Value:"))
print("1000s:",Amount//1000)
rem = Amount % 1000
print("500s:", rem//500)
print("Remaining:",rem%500)