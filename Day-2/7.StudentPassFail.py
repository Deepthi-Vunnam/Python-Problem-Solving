'''7. Student Pass/Fail Based on All Subjects >= 35
Question: Check if a student passed all subjects (maths, physics, chemistry). 
Explanation: Student passes only if marks in all subjects are 35 or more.
- Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail'''

Maths = int(input("Enter Maths Marks:"))
Physics = int(input("Enter Physics Marks:"))
Chemistry = int(input("Enter Chemistry Marks:"))
if (Maths >= 35) and (Physics >= 35) and (Chemistry >= 35):
    print("Pass")
else:
    print("Fail")