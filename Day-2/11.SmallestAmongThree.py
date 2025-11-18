'''11. Smallest Among Three Numbers
Question: Find the smallest number among three. 
Explanation: Use comparison logic to determine the minimum value. 
- Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4'''

A = int(input("Enter A value:"))
B = int(input("Enter B value:"))
C = int(input("Enter C value: "))
if A<=B and A<=C :
    print("Smallest is:", A)
elif B<=A and B<=C:
    print("Smallest is:", B)
else:
    print("Smallest is:", C)
