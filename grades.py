def gradeUpdate(grade):
    if grade > 89:
        gradeLabel.value = 'A'
    if grade > 79:
        gradeLabel.value = 'B'
    if grade > 70:
        gradeLabel.value = 'C'
    if grade == 70:
        gradeLabel.value = 'D'
    else:
        gradeLabel.value = 'F'

Label('Your grade is a(n):', 175, 125, font='monospace', size=26, bold=True)
gradeLabel = Label('X', 150, 175, font='monospace', size=48, bold=True)

gradeUpdate(85)
