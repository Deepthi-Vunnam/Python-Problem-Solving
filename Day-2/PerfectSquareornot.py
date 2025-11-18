n= int(input("Enter Number:"))
is_perfect = False
for i in range(1,n+1):
    if i*i == n:
        is_perfect = True
        break
if is_perfect:
    print("perfect Square")
else:
    print("Not Perfecr Square")

# or
n= int(input("Enter:"))
s = int(n**0.5)
if s**2 == n:
    print("Perfect")
else:
    print("Not")