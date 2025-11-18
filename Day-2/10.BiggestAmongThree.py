'''10. Biggest Among Three Numbers
Question: Find the biggest number among three. 
Explanation: Compare each pair of numbers using if-else conditions. 
- Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9'''

A = int(input("Enter A value:"))
B = int(input("Enter B value:"))
C = int(input("Enter C value: "))
if A>=B and A>=C :
    print("Biggest is:", A)
elif B>=A and B>=C:
    print("Biggest is:", B)
else:
    print("Biggest is:", C)
