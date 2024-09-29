submit_students = set()
for _ in range(28):
    submit_students.add(int(input().strip()))

allstudents = set(range(1, 31))
not_students = allstudents - submit_students

not_students = sorted(not_students)
print(not_students[0])
print(not_students[1])
