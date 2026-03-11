# store marks in a list
marks = [85, 78, 92, 74, 88]

# calculate total
total = sum(marks)

# calculate average
average = total / len(marks)

# determine grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

# display results
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)