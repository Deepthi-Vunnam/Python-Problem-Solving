'''9. Student Pass if Passed Any Two Subjects
Question: Check if the student passed any two out of three subjects. 
Explanation: Use a counter or logical conditions to verify two subjects >= 35.
- Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass'''


maths = int(input("Enter Maths marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
passed_subjects = 0
if maths >= 35:
    passed_subjects += 1
if physics >= 35:
    passed_subjects += 1
if chemistry >= 35:
    passed_subjects += 1

if passed_subjects >= 2:
    print("Pass")
else:
    print("Fail")
