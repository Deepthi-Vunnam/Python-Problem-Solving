A = int(input("Enter A value:"))
B = int(input("Enter B value:"))
C = int(input("Enter C value: "))
if A>=B and A>=C :
    print("Biggest is:", A)
elif B>=A and B>=C:
    print("Biggest is:", B)
else:
    print("Biggest is:", C)
