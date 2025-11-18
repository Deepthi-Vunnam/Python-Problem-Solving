'''8. Student Pass if Passed Any One Subject (>= 35)
Question: Check if the student passed at least one subject.
Explanation: Use logical OR to check if any one subject has marks >= 35. 
- Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass'''

Maths = int(input("Enter Maths Marks:"))
Physics = int(input("Enter Physics Marks:"))
Chemistry = int(input("Enter Chemistry Marks:"))
if (Maths >= 35) or (Physics >= 35) or (Chemistry >= 35):
    print("Pass")
else:
    print("Fail")