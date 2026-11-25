#import is_number can be replaced by isnumeric()

input_score = (input('input student\'s score:\\ '))
if not input_score.isnumeric():
    score = -999
else:
    score = int(input_score)

score = int(input('input student\'s score:\\ '))

# grade = "null"

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score : # >= 0:
    grade = "F"


# print(f"the student earned {("a", "an")[grade == "A" or grade == "A" or grade == "F"])
print(f"grade = {grade} ")
