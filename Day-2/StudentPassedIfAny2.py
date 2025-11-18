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
