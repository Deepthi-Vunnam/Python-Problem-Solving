# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds.
# - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12

Total_Seconds = int(input("Enter Seconds Value:"))
print("Hours:", Total_Seconds //3600)
rem = Total_Seconds%3600
print("Minutes:", rem//60)
print("Seconds:", rem%60)