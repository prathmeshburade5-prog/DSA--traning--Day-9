semester = int(input("Enter no of semester: "))

subjects = []
maximum = []

for i in range(semester):
    sub = int(input(f"Enter no of subjects in {i+1} semester: "))
    subjects.append(sub)

for i in range(semester):

    print("Marks obtained in semester", i+1, ":")

    marks = []

    for j in range(subjects[i]):

        mark = int(input())

        if mark < 0 or mark > 100:
            print("You have entered invalid mark.")
            exit()

        marks.append(mark)

    maxmark = marks[0]

    for k in marks:
        if k > maxmark:
            maxmark = k

    maximum.append(maxmark)

for i in range(semester):
    print("Maximum mark in", i+1, "semester:", maximum[i])