n = int(input())  # 학생 수
students = input().split()  # 학생들의 리스트
like_counts = {student: 0 for student in students}  # 인기도 딕셔너리

# 각 학생이 좋아하는 학생 정보를 입력 받으면서 좋아하는 학생들의 인기도를 증가
for _ in range(n):
    likes = input().split()  # 한 학생이 좋아하는 학생 목록
    for liked_student in likes:
        like_counts[liked_student] += 1  # 좋아하는 학생의 인기도 증가
sorted_students = sorted(like_counts.items(), key=lambda x: (-x[1], x[0]))

for student, count in sorted_students:
    print(student, count)