A = int(input("Enter A value:"))
B = int(input("Enter B value:"))
C = int(input("Enter C value: "))
if A<=B and A<=C :
    print("Smallest is:", A)
elif B<=A and B<=C:
    print("Smallest is:", B)
else:
    print("Smallest is:", C)
