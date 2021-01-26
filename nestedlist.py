students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
students = sorted(students, key = lambda x:x[1])
seclowest_score = sorted(list (set([x[1]for x in students])))[1]
students2 = []
for i in students:
    if i[1] == seclowest_score:
        students2.append(i[0])
print("\n".join(sorted(students2)))