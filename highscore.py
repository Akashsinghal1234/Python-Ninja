# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
a = 0
for max_marks in student_scores:
    if max_marks > a:
        a = max_marks 

print(f"highest marks are {a}")






