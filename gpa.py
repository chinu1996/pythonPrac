print('welcome to the GPA Calculator')
print('please enter all your grades, one per line')
points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 1.67, 'D+': 1.33,
          'D': 1.0}
courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == "":  # To read line from the user
        done = True
    elif grade not in points:
        print("Unknown grade'{0}' being ignored".format(grade))
    else:
        courses += 1
        total_points += points[grade]
if courses > 0:  # to avaoid division by zero
    print('Your GPA is {0:.3}'.format(total_points / courses))
print(points)
