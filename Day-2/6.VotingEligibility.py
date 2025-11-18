# 6. Voting Eligibility
# Question: Check if a person is eligible to vote (age >= 18). Explanation: 
# A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote

Age = int(input("Enter Age:"))
if (Age >= 18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")